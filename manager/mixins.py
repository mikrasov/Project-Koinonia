import json, urllib

from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from manager.models import Pack, Character, Ability, Attribute

#Generic Mixins
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
    

class PermissionEditMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().can_edit(request.user):
            return HttpResponseRedirect('/login')
        return super(PermissionEditMixin, self).dispatch(request, *args, **kwargs)

class PermissionViewMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().can_view(request.user):
            return HttpResponseRedirect('/login')
        return super(PermissionViewMixin, self).dispatch(request, *args, **kwargs)
        
class JsonIoMixin(object):    
    IO_VERSION = 1.01

    def import_json(self, postData):
        data = json.loads(postData)
        
        charactersToAdd = []
        charactersExisting = []
        abilityToAdd = []
        attributeToAdd = []

        # Existing characters
        existingCharacters = Character.objects.filter(pack=self.object)
        for character in data["characters"]:
            #Skip blank character name
            if character["name"] =='':
                continue
            
            importedChar = Character(pack=self.object)
            importedChar.name = character["name"]
            importedChar.slug = slugify(character["name"])
                
            importedChar.avatar = character["avatar"] or ""
            importedChar.token = character.get("token") or ""
            
            importedChar.bio = urllib.parse.unquote(character["bio"] or "")
            importedChar.gmnotes = urllib.parse.unquote(character["gmnotes"] or "")
            
            if existingCharacters.filter(name=character["name"]).exists():
                charactersExisting.append(importedChar)
                character["alreadyExists"] = True
            else:
                charactersToAdd.append(importedChar)
                character["alreadyExists"] = False
            
        Character.objects.bulk_create(charactersToAdd)

        packChars = Character.objects.filter(pack=self.object)
        for character in data["characters"]:    
            if not character["alreadyExists"]:
                onChar = packChars.get(name=character["name"]);
                for ability in character["abilities"]:
                    importedAbility = Ability(character=onChar)
                    importedAbility.name = ability["name"]
                    importedAbility.action = ability["action"]
                    importedAbility.istokenaction = ability["istokenaction"]
                    abilityToAdd.append(importedAbility)
                
                for attribute in character["attributes"]:
                    importedAttribute = Attribute(character=onChar)
                    importedAttribute.name = attribute["name"]
                    importedAttribute.current = attribute["current"]
                    importedAttribute.max = attribute["max"]
                    attributeToAdd.append(importedAttribute)
            
        Ability.objects.bulk_create(abilityToAdd)
        Attribute.objects.bulk_create(attributeToAdd)

    def export_json(self):
        exportObj = {}
        exportObj["version"] = JsonIoMixin.IO_VERSION
        exportObj["characters"] = []
        
        packChars = Character.objects.filter(pack=self.object)
        for character in packChars:    
            exportChar = {}
            exportChar["name"] = character.name
            
            exportChar["abilities"] = []
            for ability in Ability.objects.filter(character=character):
                exportedAblity = {}
                exportedAblity["name"] = ability.name
                exportedAblity["action"] = ability.action
                exportedAblity["istokenaction"] = ability.istokenaction
                exportChar["abilities"].append(exportedAblity)
            
            exportChar["attributes"] = []
            for attribute in Attribute.objects.filter(character=character):
                exportedAttribute = {}
                exportedAttribute["name"] = attribute.name
                exportedAttribute["current"] = attribute.current
                exportedAttribute["max"] = attribute.max
                exportChar["attributes"].append(exportedAttribute)
                
            exportObj["characters"].append(exportChar)
        return json.dumps(exportObj);