from django import template
from django.db.models.query import QuerySet

register = template.Library()

@register.filter(name='canView')
def canViewFilter(user, value):
    if isinstance(value, QuerySet):
        return [obj for obj in value if obj.can_view(user)] 
    else:
        return value.can_view(user);

@register.filter(name='canEdit')
def canEditFilter(user, value):
    if isinstance(value, QuerySet):
        return [obj for obj in value if obj.can_edit(user)] 
    else:
        return value.can_edit(user);