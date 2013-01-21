# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
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


def get_shells(request):
    if request.method == 'GET':
        city_id = request.GET.get('id_city', -1)
        if(city_id != -1):
            result = map(lambda code: borderdata.get_data_by_port(code),
                geolocal.get_border_codes(city_id))
    else:
        result = []
    return render_to_response('shells.html', {'ports': result},
        context_instance=RequestContext(request))


def what_is_my_ip(request):
    return HttpResponse(request.META['REMOTE_ADDR'])
