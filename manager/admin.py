from django.contrib import admin
from manager.models import Pack, Character, Ability, Attribute

class AbilityInline(admin.TabularInline):
    model = Attribute

class AttributesInline(admin.TabularInline):
    model = Ability    
    
class PackAdmin(admin.ModelAdmin):
    list_display = ('name','system', 'date_created')


class CharacterAdmin(admin.ModelAdmin):
    inlines = [AbilityInline, AttributesInline]
    list_display = ('name','source')

# Register your models here.
admin.site.register(Pack, PackAdmin)
admin.site.register(Character, CharacterAdmin)
