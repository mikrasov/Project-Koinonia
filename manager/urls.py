from django.conf.urls import patterns, url

from manager import views

urlpatterns = patterns('',
    url(r'^$', views.PackListView.as_view(), name='pack-list'),
        
    url(r'^(?P<pk>\d+)/$', views.PackDetailView.as_view(), name='pack-detail'),
    url(r'^(?P<pk>\d+)/results/$', views.PackResultsView.as_view(), name='results'),
    
    url(r'^(?P<pack_id>\d+)/vote/$', views.vote, name='vote'),
)