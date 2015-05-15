from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.views import generic
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from manager.models import Pack, Character
from manager.forms import PackForm, CharacterForm, CharacterNotesForm, AbilityFormSet, AttributeFormSet, PackExportForm
from manager.mixins import JsonIoMixin, PermissionViewMixin, PermissionEditMixin, LoginRequiredMixin

# Pack Views
class PackListView(generic.ListView):
    
    def get_queryset(self):
        order_by = self.request.GET.get('order_by', '-date_created')
        return Pack.objects.order_by(order_by)

class PackDetailView(PermissionViewMixin, generic.DetailView):
    model = Pack

class PackCreateView(LoginRequiredMixin, generic.CreateView):
    model = Pack
    form_class = PackForm
    success_url = '../'
    template_name_suffix = '_edit'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.slug = slugify(form.instance.name)
        return super(PackCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return self.object.get_absolute_url()

class PackUpdateView(PermissionEditMixin, generic.UpdateView):
    model = Pack
    form_class = PackForm
    template_name_suffix = '_edit'
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super(PackUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        return self.object.get_absolute_url()
    
class PackImportView(PermissionEditMixin, JsonIoMixin, generic.detail.SingleObjectMixin, generic.View):
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
        
class PackExportView(PermissionViewMixin, generic.detail.SingleObjectMixin, generic.View):
    template_name = 'pack_export.html'
    model = Pack

    def get(self, request, *args, **kwargs):
        return render(request, 'manager/pack_export.html', {
            'title': self.get_object().name,
            'form_action': reverse("manager:export"),
            'character_list': self.get_object().character_set.order_by('name'),
        })

class PackDeleteView(PermissionEditMixin, generic.DeleteView):
    model = Pack
    success_url = '../../../'
        
# Character views
    
class CharacterDetailView(PermissionViewMixin, generic.DetailView):
    model = Character

class CharacterCreateView(LoginRequiredMixin, generic.CreateView):
    model = Character
    form_class = CharacterForm
    success_url = '../'
    template_name_suffix = '_edit'

    def get_success_url(self):
        return self.object.get_absolute_url()
    
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        notes_form = CharacterNotesForm()
        ability_form = AbilityFormSet()
        attribute_form = AttributeFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  notes_form = notes_form,
                                  ability_form=ability_form,
                                  attribute_form=attribute_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        notes_form = CharacterNotesForm(self.request.POST)
        ability_form = AbilityFormSet(self.request.POST)
        attribute_form = AttributeFormSet(self.request.POST)
        if (form.is_valid() and  notes_form.is_valid() and ability_form.is_valid() and
            ability_form.is_valid()):
            return self.form_valid(form, notes_form, ability_form, ability_form)
        else:
            return self.form_invalid(form, notes_form,  attribute_form, attribute_form)
        
    def form_valid(self, form, notes_form, ability_form, attribute_form):
        form.instance.owner = self.request.user
        form.instance.slug = slugify(form.instance.name)
        self.object = form.save()
        notes_form.instance = self.object
        notes_form.save()
        ability_form.instance = self.object
        ability_form.save()
        attribute_form.instance = self.object
        attribute_form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form, notes_form, ability_form, attribute_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  notes_form = notes_form,
                                  ability_form=ability_form,
                                  attribute_form=attribute_form))
        
    
    
class CharacterUpdateView(PermissionEditMixin, generic.UpdateView):
    model = Character
    form_class = CharacterForm
    template_name_suffix = '_edit'
    
    def get_success_url(self):
        return self.object.get_absolute_url()
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        notes_form = CharacterNotesForm(instance=self.object)
        ability_form = AbilityFormSet(instance=self.object)
        attribute_form = AttributeFormSet(instance=self.object)
        return self.render_to_response(
            self.get_context_data(form=form,
                                  notes_form = notes_form,
                                  ability_form=ability_form,
                                  attribute_form=attribute_form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        notes_form = CharacterNotesForm(self.request.POST)
        ability_form = AbilityFormSet(self.request.POST)
        attribute_form = AttributeFormSet(self.request.POST)
        if (form.is_valid() and  notes_form.is_valid() and ability_form.is_valid() and
            ability_form.is_valid()):
            return self.form_valid(form, notes_form, ability_form, ability_form)
        else:
            return self.form_invalid(form, notes_form, attribute_form, attribute_form)
    
    def form_valid(self, form, notes_form, ability_form, attribute_form):
        form.instance.owner = self.request.user
        form.instance.slug = slugify(form.instance.name)
        self.object = form.save()
        notes_form.instance = self.object
        notes_form.save()
        ability_form.instance = self.object
        ability_form.save()
        attribute_form.instance = self.object
        attribute_form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form, notes_form, ability_form, attribute_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  notes_form = notes_form,
                                  ability_form=ability_form,
                                  attribute_form=attribute_form))

class CharacterExportView(PermissionViewMixin, generic.detail.SingleObjectMixin, generic.View):
    template_name = 'pack_export.html'
    model = Character

    def get(self, request, *args, **kwargs):
        return render(request, 'manager/pack_export.html', {
            'title': self.get_object().name,
            'form_action': reverse("manager:export"),
            'character_list': [self.get_object()],
        })
        
class CharacterDeleteView(PermissionEditMixin, generic.DeleteView):
    model = Character
    success_url = '../../../'
    
class ExportView(JsonIoMixin, generic.View):
    template_name = 'pack_export.html'
    
    def get(self, request, *args, **kwargs):
        return HttpResponseNotFound('<h1>Page was found</h1>')

    def post(self, request, *args, **kwargs):
        character_ids = request.POST.getlist("characters");
        character_list = Character.objects.in_bulk(character_ids).values()
        exportAttributes = request.POST.getlist("attributes")
        exportedAblities = request.POST.getlist("abilities")
        exportBios= request.POST.getlist("bio")
        exportNotes= request.POST.getlist("notes")
        export_json = self.export_json(character_list, exportAttributes, exportedAblities, exportBios, exportNotes);
            
        #exportAttributes, exportedAblities, exportBios, exportNotes
        return render(request, 'manager/export.html', {
            'exportedJson': export_json,                    
            'character_list': character_list,
        })