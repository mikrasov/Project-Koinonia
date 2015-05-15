from django.conf.urls import patterns, url

from manager import views

urlpatterns = patterns('',
    url(r'^$', views.PackListView.as_view(), name='index'),
    
    url(r'^export/$', views.ExportView.as_view(), name='export'),
    
    url(r'^pack/$', views.PackListView.as_view(), name='pack-list'), 
    url(r'^pack/create/$', views.PackCreateView.as_view(), name='pack-create'), 
    url(r'^pack/(?P<slug>[-\w\d]+),(?P<pk>\d+)/$', views.PackDetailView.as_view(), name='pack-detail'),
    url(r'^pack/(?P<slug>[-\w\d]+),(?P<pk>\d+)/update/$', views.PackUpdateView.as_view(), name='pack-update'),
    url(r'^pack/(?P<slug>[-\w\d]+),(?P<pk>\d+)/delete/$', views.PackDeleteView.as_view(), name='pack-delete'),    
    url(r'^pack/(?P<slug>[-\w\d]+),(?P<pk>\d+)/import/$', views.PackImportView.as_view(), name='pack-import'),    
    url(r'^pack/(?P<slug>[-\w\d]+),(?P<pk>\d+)/export/$', views.PackExportView.as_view(), name='pack-export'),    
    
    url(r'^character/create/$', views.CharacterCreateView.as_view(), name='character-create'), 
    url(r'^character/(?P<slug>[-\w\d]+),(?P<pk>\d+)/$', views.CharacterDetailView.as_view(), name='character-detail'),
    url(r'^character/(?P<slug>[-\w\d]+),(?P<pk>\d+)/update/$', views.CharacterUpdateView.as_view(), name='character-update'),
    url(r'^character/(?P<slug>[-\w\d]+),(?P<pk>\d+)/delete/$', views.CharacterDeleteView.as_view(), name='character-delete'),
    url(r'^character/(?P<slug>[-\w\d]+),(?P<pk>\d+)/export/$', views.CharacterExportView.as_view(), name='character-export'),
)