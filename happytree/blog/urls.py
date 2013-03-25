#coding=utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'happytree.views.home', name='home'),
    # url(r'^happytree/', include('happytree.foo.urls')),
	(r'^$',home),
	(r'^add/post_article/$',post_article),
	(r'^add/$',add_article),
	(r'^show/(?P<a_id>\d+)/$', show_article),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
