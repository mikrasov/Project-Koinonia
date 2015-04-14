from django.contrib import admin
from manager.models import Pack, Character, Ability, Attribute

class AbilityInline(admin.TabularInline):
    model = Attribute

class AttributesInline(admin.TabularInline):
    model = Ability    

class CharacterInline(admin.TabularInline):
    model = Character
    fields = ('name', 'source', 'slug')
    show_change_link = True;
        
class PackAdmin(admin.ModelAdmin):
    search_fields = ('name', 'system', 'owner')
    list_display = ('name', 'system', 'owner', 'date_created','date_modified')
    list_filter = ('date_created','date_modified')
    inlines = [CharacterInline]
    
class CharacterAdmin(admin.ModelAdmin):
    search_fields = ('name', 'source')
    list_display = ('name', 'source', 'date_created','date_modified','pack')
    list_filter = ('date_created','date_modified')
    inlines = [AbilityInline, AttributesInline]
    
# Register your models here.
admin.site.register(Pack, PackAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Ability)
admin.site.register(Attribute)
