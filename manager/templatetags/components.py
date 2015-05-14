from django import template

register = template.Library()

@register.simple_tag
def panel( panel_id="", panel_title="", panel_show_action=False, panel_action=""):
    str =  '<div class="panel panel-default">'
    str += '<div class="panel-heading" data-toggle="collapse" data-target="#'+panel_id+'">'
    if panel_show_action:
        str += '<div class="actions pull-right">'+panel_action+'</div>'           
    str += '<h3>'+panel_title+'</h3>'
    str += '</div>'
    str += '<div class="panel-body panel-collapse collapse in" id="'+panel_id+'">'
    return str

@register.simple_tag
def endpanel():
    str = '</div>'
    str += '<div class="panel-footer"></div>'
    str += '</div>'
    return str
