import json

from django.core import serializers
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic

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
        return super(PackCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('manager:pack-detail', kwargs={'pk': self.object.id})

class PackUpdateView(OwnerCheckMixin, generic.UpdateView):
    model = Pack
    template_name_suffix = '_edit'
    fields = ['name', 'system']
    
    def get_success_url(self):
        return reverse('manager:pack-detail', kwargs={'pk': self.object.id})

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
 
            for character in data["characters"]:
                importedChar = Character.objects.create(pack=self.object)
                importedChar.name = character["name"]
                importedChar.save()
                
                for ability in character["abilities"]:
                    importedAbility = Ability.objects.create(character=importedChar)
                    importedAbility.name = ability["name"]
                    importedAbility.action = ability["action"]
                    importedAbility.istokenaction = ability["istokenaction"]
                    importedAbility.save()
                for attribute in character["attributes"]:
                    importedAttribute = Attribute.objects.create(character=importedChar)
                    importedAttribute.name = attribute["name"]
                    importedAttribute.current = attribute["current"]
                    importedAttribute.max = attribute["max"]
                    importedAttribute.save()
                    
            return HttpResponseRedirect(reverse('manager:pack-detail', kwargs={'pk': self.object.pk}))
    
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
        return reverse('manager:character-detail', kwargs={'pk': self.object.id})


class CharacterDeleteView(OwnerCheckMixin, generic.DeleteView):
    model = Character
    success_url = '../../../'