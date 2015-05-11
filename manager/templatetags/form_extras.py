from django import template

register = template.Library()

@register.filter(name='addatrr')
def addatrr(field, attr):
    if not field:
        return field
    listAttribute = attr.split('=',1)
    if len(listAttribute) <2:
        return field
    return field.as_widget(attrs={listAttribute[0]:listAttribute[1]})