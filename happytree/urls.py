#!/usr/bin/env python
#coding=utf-8
from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'happytree.views.home', name='home'),
    # url(r'^happytree/', include('happytree.foo.urls')),
	(r'^$',index.hello),
	#(r'^static/',index.test),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	#
	#(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
	#url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}, name='static'),
)

urlpatterns += patterns('',
	(r'^blog/',include('happytree.blog.urls')),
)
print settings.STATIC_ROOT

if settings.DEBUG:
	#urlpatterns += staticfiles_urlpatterns()
	print  staticfiles_urlpatterns()
