# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


def to_tuple(x):
    return zip(x, x)


class MexCity(models.Model):
    STATE_NAME = (
        'Baja California',
        'Sonora',
        'Chihuahua',
        'Coahuila',
        'Nuevo Leon',
        'Tamaulipas'
    )

    name = models.CharField(max_length=60)
    state = models.CharField(max_length=30, choices=to_tuple(STATE_NAME))
    link = models.CharField(max_length=40)

    def __unicode__(self):
        return unicode("%s %s" % (self.name, self.state))

    def get_absolute_url(self):
        return reverse("alias_url", args=(self.link,))


class Border(models.Model):
    border_id = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    city = models.ForeignKey(MexCity)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return unicode("%s" % (self.name))

    # get latitudes list
    @staticmethod
    def get_coords():
        return [(field.latitude, field.longitude, field.city.id)\
            for field in list(Border.objects.all())]

    @staticmethod
    def get_border_codes(city_id):
        return [field.border_id for field in list(Border.objects.filter(city__id=city_id))]
