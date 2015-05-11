from django import forms
from django.forms import ModelForm, Form
from django.forms.models import inlineformset_factory

from manager.models import Pack, Character, Ability, Attribute

class PackForm(ModelForm):
    class Meta:
        model = Pack
        fields = ['name', 'system','isPublic']
        
class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'source', 'token', 'avatar']

class CharacterNotesForm(ModelForm):
    class Meta:
        model = Character
        fields = ['bio', 'gmnotes']
        
AbilityFormSet = inlineformset_factory(Character, Ability, fields=('name','action','istokenaction'))
AttributeFormSet = inlineformset_factory(Character, Attribute, fields=('name','current','max'))

class PackExportForm(Form):
    detail = forms.BooleanField()