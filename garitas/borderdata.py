from urllib2 import urlopen
from garitas import xmltodict
from garitas.models import Border, MexCity
from garitas.utils import time_format


class BorderData():
    def get_data_by_port(self, port_number):
        response = urlopen("http://apps.cbp.gov/bwt/bwt.xml").read()
        #response  = open("bwt.xml", "r").read()
        ports_list = list(xmltodict.parse(response)["border_wait_time"]["port"])
        for port in ports_list:
            if port['port_number'] == port_number:
                return self.__get_port_data(port)

    def get_city_name(self, city_id):
        city_name = self.__get_city_data(city_id)
        return city_name if city_name != -1 else ""

    def get_city_by_alias(self, alias):
        city = MexCity.objects.filter(link=alias)
        return city[0].id if city.exists() else -1

    def get_cities_list(self):
        return Border.objects.all()

    def __get_port_data(self, port):
        return {
            "mx_alias": Border.objects.get(border_id=port['port_number']).name,
            "vehicle_standard_lane": self.__get_delay_time_format(\
                port['passenger_vehicle_lanes']['standard_lanes']['delay_minutes']),
            "vehicle_sentri_lane": self.__get_delay_time_format(\
                port['passenger_vehicle_lanes']['NEXUS_SENTRI_lanes']['delay_minutes']),
            "vehicle_ready_lane": self.__get_delay_time_format(\
                port['passenger_vehicle_lanes']['ready_lanes']['delay_minutes']),
            "pedestrian_standard_lanes": self.__get_delay_time_format(\
                port['pedestrian_lanes']['standard_lanes']['delay_minutes']),
        }

    def __get_city_data(self, city_id):
        return {
            "mx_city": self.__get_mx_city(city_id) if city_id > 0 else -1
        }

    def __get_mx_city(self, city_id):
        mex_city = MexCity.objects.get(id=city_id)
        state = mex_city.state
        city = mex_city.name
        return "%s - %s" % (city, state)

    def __get_delay_time_format(self, delay_time):
        time = time_format(delay_time)
        return {
            'hours': time[0],
            'mins': time[1],
            'color': self.__get_delay_color(time[0], time[1]),
            'time_text': 'min' if (time[0] == "0") else 'hrs' if (time[0] != "--") else "",
        }

    def __get_delay_color(self, delay_hrs, delay_min):
        if(delay_hrs == '--' or delay_min == '--'):
            return '666'
        elif(int(delay_hrs) >= 1):
            return 'FF6666'
        elif(int(delay_min) <= 15):
            return '33CCCC'
        elif(int(delay_hrs) <= 59):
            return '63C502'


borderdata = BorderData()
