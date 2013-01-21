from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^borders/$', 'api.views.get_by_coords', name="api_coords"),
    url(r'^borders/(?P<city_id>[-\w]+)/$', 'api.views.borders', name="api_border"),
)
