from django.conf.urls import patterns, url

from manager import views

urlpatterns = patterns('',
    url(r'^$', views.PackListView.as_view(), name='pack-list'),
    url(r'^pack/(?P<pk>\d+)/$', views.PackDetailView.as_view(), name='pack-detail'),
    url(r'^pack/create/$', views.PackCreateView.as_view(), name='pack-create'),    
    url(r'^pack/update/(?P<pk>\d+)/$', views.PackUpdateView.as_view(), name='pack-update'),    
    url(r'^pack/import/(?P<pk>\d+)/$', views.PackImportView.as_view(), name='pack-import'),    
    url(r'^pack/export/(?P<pk>\d+)/$', views.PackExportView.as_view(), name='pack-export'),    
    url(r'^pack/delete/(?P<pk>\d+)/$', views.PackDeleteView.as_view(), name='pack-delete'),    
    
    
    url(r'^character/$', views.CharacterListView.as_view(), name='character-list'),
    url(r'^character/(?P<pk>\d+)/$', views.CharacterDetailView.as_view(), name='character-detail'),
    url(r'^character/update/(?P<pk>\d+)/$', views.CharacterUpdateView.as_view(), name='character-update'),
    url(r'^character/delete/(?P<pk>\d+)/$', views.CharacterDeleteView.as_view(), name='character-delete'),
    
    
)