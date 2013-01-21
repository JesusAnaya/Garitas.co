from urllib2 import urlopen, HTTPError
from models import Border
from django.utils import simplejson
from math import sqrt, pow


class Geolocal():

    def get_border_codes(self, city_id):
        return Border.get_border_codes(city_id)

    """
    function get_city_id: return the city id from your position using your ip address

    dir_ip: your current public ip address

    return: return the id city from your city or -1 if your city is over to cities list
    """
    def get_city_id(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip_adds = request.META['HTTP_X_FORWARDED_FOR'].split(",")
            ip = ip_adds[0]
        else:
            ip = request.META['REMOTE_ADDR']
        current_pos = self.__get_current_coords(self.__parse_ip(ip))
        print self.__parse_ip(ip)
        #if(current_pos[0] != 0 and current_pos[1] != 0):
        if current_pos != -1:
            return self.__get_id_city_by_coords(current_pos, Border.get_coords())
        return -1

    def __parse_ip(self, ip):
        try:
            if(ip == '127.0.0.1'):
                return urlopen("http://garitas.co/whatismyip/").read()
        except HTTPError, e:
            print(e.code)
        return ip

    """
    function __get_current_coords: get your ip geolocalitation information and serialize the response

    dir_ip: your current public ip address

    return: return a tuple with your current position (latitude, longitude)
    """
    def __get_current_coords(self, dir_ip):
        try:
            #get json array with all information about your IP Address and serialized to object
            result = simplejson.loads(urlopen("http://api.easyjquery.com/ips/?ip=%s&full=true"\
                % dir_ip).read())
            #create a tuple with current position usind the latitude and longitude values
            return (result['CityLatitude'], result['CityLongitude'])
        except HTTPError, e:
            print(e.code)
        return -1

    """
    function __get_id_city_by_coords: get the id from the city most close to your current position

    search: current coords
    coords: list of all coords

    return: return the city id from coord list or -1 in error case
    """
    def __get_id_city_by_coords(self, search, coords):
        near = map(lambda x: sqrt(pow(search[0] - x[0], 2) + pow(search[1] - x[1], 2)), coords)
        x = min(near)
        # get id city from 3rd parameter from a tuple of coords list
        return coords[near.index(x)][2] if x < 2 else -1


# make a geolocal object
geolocal = Geolocal()
