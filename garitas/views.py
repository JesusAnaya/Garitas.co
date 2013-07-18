# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson as json
from django.conf import settings
from garitas.geolocal import geolocal
from garitas.borderdata import borderdata
from garitas.models import MexCity
from garitas.email import send_response_mail


def home(request, city=None):
    #search permalinks in the url
    if city is not None:
        city_id = borderdata.get_city_by_alias(city)
    else:
        city_id = geolocal.get_city_id(request)
    city_info = borderdata.get_city_name(city_id)
    cities = map(
        lambda city: {
            'state': city.state,
            'city': city.name,
            'alias': city.link
        }, MexCity.objects.all()
    )
    return render_to_response('home.html', {
        'city': city_info,
        'city_id': city_id,
        'cities': cities
    }, context_instance=RequestContext(request))


def send_email(request):
    success = True
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_response_mail(
            settings.EMAI_CONTACT, 'Garitas - Feedback',
            "emails/send_feedback.html", {
                'name': name,
                'email': email,
                'tel': tel,
                'subject': subject,
                'message': message
            })
    else:
        success = False
    return HttpResponse(json.dumps({'success': success}), mimetype="application/json")


def what_is_my_ip(request):
    return HttpResponse(request.META['REMOTE_ADDR'])
