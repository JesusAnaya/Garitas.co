# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from garitas.geolocal import geolocal
from garitas.borderdata import borderdata
from garitas.models import MexCity


def home(request, city=None):
    #search permalinks in the url
    if city is not None:
        city_id = borderdata.get_city_by_alias(city)
    else:
        city_id = geolocal.get_city_id(request)
    city_info = borderdata.get_city_name(city_id)
    cities = map(lambda city: {
            'state': city.state,
            'city': city.name,
            'alias': city.link
        }, MexCity.objects.all()
    )
    return render_to_response('home.html', {
        'city': city_info,
        'city_id': city_id,
        'cities': cities}
    )


def what_is_my_ip(request):
    return HttpResponse(request.META['REMOTE_ADDR'])
