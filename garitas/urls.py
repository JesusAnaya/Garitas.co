# -*- coding: utf-8 -*-
try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

from garitas import sitemap

urlpatterns = patterns('',
    url(r'^$', 'garitas.views.home', name='home'),
    url(r'^send_email/$', 'garitas.views.send_email', name='send_email'),
    url(r'^whatismyip/$', 'garitas.views.what_is_my_ip', name='whatismyip'),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
        'sitemaps': {
            'url': sitemap.GaritasSitemap
        }
    }),
    #get any word as posible city name if this is not resolved before
    url(r'^(?P<city>[-\w]+)/$', 'garitas.views.home', name='alias_url'),
)
