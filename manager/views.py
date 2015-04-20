import json

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.text import slugify

from manager.models import Pack, Character
from manager.mixins import JsonIoMixin, OwnerCheckMixin, LoginRequiredMixin

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
    
    can_edit = "bob"
    
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

class PackImportView(JsonIoMixin, OwnerCheckMixin, generic.detail.SingleObjectMixin, generic.View):
    model = Pack
    template_name_suffix = '_import'

    def post(self, request, *args, **kwargs):
        # Look up the pack
        self.object = self.get_object()
                
        #try:
        self.import_json(request.POST["import_data"])
        return HttpResponseRedirect( self.object.get_absolute_url() )
        #except ValueError:
            # If Invalid JSON
        #    return render(request, 'manager/pack_import.html', {
        #        'pack': self.object,
        #        'error_message': "Invalid JSON",
        #    })
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, 'manager/pack_import.html', {
            'pack': self.object,
        })
        
class PackExportView(JsonIoMixin, LoginRequiredMixin, generic.detail.SingleObjectMixin, generic.View):
    model = Pack   
    
    can_edit = "bob"
    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        
        return render(request, 'manager/pack_export.html', {
            'pack': self.object,
            'exportedJson': self.export_json(),
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
    fields = ['name', 'source', 'token', 'avatar', 'bio', 'gmnotes']
    
    def get_success_url(self):
        return self.object.get_absolute_url()


class CharacterDeleteView(OwnerCheckMixin, generic.DeleteView):
    model = Character
    success_url = '../../../'