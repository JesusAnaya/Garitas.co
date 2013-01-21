from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^borders/(?P<city_id>[-\w]+)/$', 'api.views.borders', name="api_cities"),
)
