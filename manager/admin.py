from django.contrib import admin
from manager.models import Pack, Character

class CharacterInline(admin.TabularInline):
    model = Character
    
class PackAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'date_created')
    inlines = [CharacterInline]
		
# Register your models here.
admin.site.register(Pack, PackAdmin)