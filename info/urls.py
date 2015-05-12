from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from info import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="info/index.html"), name='index'),
    url(r'^user/(?P<username>\w+)$', views.ProfileDetailView.as_view(), name='profile-detail'), 
    url(r'^login/$', TemplateView.as_view(template_name="info/login.html"), name='login'),
)