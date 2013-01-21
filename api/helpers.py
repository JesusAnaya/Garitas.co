#-*- coding: utf-8 -*-
from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder


def json_dumps(data, **options):
    """
    Wrapper around `simplejson.dumps` that uses a special JSON encoder.
    """
    params = {'sort_keys': True, 'indent': 2}
    params.update(options)
    # This code is based off django's built in JSON serializer
    if simplejson.__version__.split('.') >= ['2', '1', '3']:
        # Use JS strings to represent Python Decimal instances (ticket #16850)
        params.update({'use_decimal': False})
    return simplejson.dumps(data, cls=DjangoJSONEncoder, **params)
