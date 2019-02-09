import urllib.request
from requests.utils import requote_uri
import json

class Api:
    def __init__(self):
        self.base_url = 'http://api.population.io:80/1.0'
    def countries(self):
        endpoint = '/countries'
        country_json = self.__fetch_endpoint(endpoint)
        return country_json['countries']

    def population_by_year_and_age(self, year, age):
        endpoint = f'/population/{year}/aged/{age}'
        pass
    
    def population_by_year_country_and_age(self, year, country, age):
        endpoint = f'/population/{year}/{country}/{age}/'
        pass
    
    def population_by_year_and_country(self, year, country):
        endpoint = f'/population/{year}/{country}/'
        pass

    def population_by_country_and_age(self, country, age):
        endpoint = f'/population/{country}/{age}/'
        pass

    def population_by_country_and_date(self, country, date):
        endpoint = f'/population/{country}/{date}/'
        pass

    def population_by_country_today_and_tomorrow(self, country):
        endpoint = f'/population/{country}/today-and-tomorrow/'
        pass

    def __fetch_endpoint(self, endpoint):
        full_url = requote_uri(self.base_url + endpoint)
        binary_data = urllib.request.urlopen(full_url).read()
        text_data = binary_data.decode('utf-8')
        return json.loads(text_data)