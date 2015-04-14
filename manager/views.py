import json
import uuid

from django.core import serializers
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.text import slugify

from manager.models import Pack, Character, Ability, Attribute
from manager.mixins import OwnerCheckMixin, LoginRequiredMixin

# Pack Views
class PackListView(generic.ListView):
    
    def get_queryset(self):
        order_by = self.request.GET.get('order_by', '-date_created')
        return Pack.objects.order_by(order_by)

class PackDetailView(generic.DetailView):
    model = Pack

class PackCreateView(LoginRequiredMixin, generic.CreateView):
    model = Pack
    success_url = '../'
    template_name_suffix = '_edit'
    fields = ['name', 'system']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.slug = slugify(form.instance.name)
        return super(PackCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return self.object.get_absolute_url()

class PackUpdateView(OwnerCheckMixin, generic.UpdateView):
    model = Pack
    template_name_suffix = '_edit'
    fields = ['name', 'system']
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super(PackUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        return self.object.get_absolute_url()

class PackImportView(OwnerCheckMixin, generic.detail.SingleObjectMixin, generic.View):
    model = Pack
    template_name_suffix = '_import'

    def post(self, request, *args, **kwargs):
        # Look up the pack
        self.object = self.get_object()
                
        try:
            data = json.loads(request.POST["import_data"])
         
        except ValueError:
            # Invalid JSON
            return render(request, 'manager/pack_import.html', {
                'pack': self.object,
                'error_message': "Invalid JSON",
            })
        else:
 
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
                    
            return HttpResponseRedirect( self.object.get_absolute_url() )
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, 'manager/pack_import.html', {
            'pack': self.object,
        })
        
class PackExportView(LoginRequiredMixin, generic.detail.SingleObjectMixin, generic.View):
    model = Pack   
    
    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        
        exportData = serializers.serialize("json", [self.get_object() ])
        
        return render(request, 'manager/pack_export.html', {
            'pack': self.object,
            'exportedJson': exportData,
        })
        
         
class PackDeleteView(OwnerCheckMixin, generic.DeleteView):
    model = Pack
    success_url = '../../../'
        
# Character views
class CharacterListView(generic.ListView):
    model = Character
    
class CharacterDetailView(generic.DetailView):
    model = Character

class CharacterUpdateView(OwnerCheckMixin, generic.UpdateView):
    model = Character
    template_name_suffix = '_edit'
    fields = ['name', 'source', 'bio', 'gmnotes']
    
    def get_success_url(self):
        return self.object.get_absolute_url()


class CharacterDeleteView(OwnerCheckMixin, generic.DeleteView):
    model = Character
    success_url = '../../../'