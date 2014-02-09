import os
from django.conf.urls import patterns, include, url
from sigmaintro.views import *
from django.contrib import admin
#admin.autodiscover()
site_media = os.path.join(
     os.path.dirname(__file__), 'site_media'
   )

urlpatterns = patterns('',
    (r'^$', home),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
    # Examples:
    # url(r'^$', home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
