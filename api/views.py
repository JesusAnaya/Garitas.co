#-*- coding: utf-8 -*-
from django.http import HttpResponse
from garitas.borderdata import borderdata
from garitas.geolocal import geolocal
from api.helpers import json_dumps


def borders(request, city_id=None):
    result = []
    if city_id is not None:
        result = map(lambda code: borderdata.get_data_by_port(code),
            geolocal.get_border_codes(city_id))
    return HttpResponse(json_dumps(result), mimetype='application/json')
