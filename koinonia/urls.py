from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'koinonia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^browse/', include('manager.urls', namespace="manager")),
    url('', include('info.urls', namespace="info")),
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    

)
