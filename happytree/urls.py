#!/usr/bin/env python
#coding=utf-8
from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'happytree.views.home', name='home'),
    # url(r'^happytree/', include('happytree.foo.urls')),
	(r'^$',index.hello),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}, name='static'),
)

urlpatterns += patterns('',
	(r'^blog/',include('happytree.blog.urls')),
)

from django.conf.urls.defaults import *
handler404 = 'index.my_404_view'
handler500 = 'index.my_500_view'
