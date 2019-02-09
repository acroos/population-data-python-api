import urllib.request
from requests.utils import requote_uri
import json
from population_data_factory import PopulationDataFactory

class Api:
    def __init__(self):
        self.base_url = 'http://api.population.io:80/1.0'

    def countries(self):
        endpoint = '/countries'
        country_json = self.__fetch_endpoint(endpoint)
        return country_json['countries']

    def population_by_year_and_age(self, year, age):
        endpoint = f'/population/{year}/aged/{age}/'
        return self.__year_data_from_endpoint(endpoint)
    
    def population_by_year_country_and_age(self, year, country, age):
        endpoint = f'/population/{year}/{country}/{age}/'
        return self.__year_data_from_endpoint(endpoint)
    
    def population_by_year_and_country(self, year, country):
        endpoint = f'/population/{year}/{country}/'
        return self.__year_data_from_endpoint(endpoint)

    def population_by_country_and_age(self, country, age):
        endpoint = f'/population/{country}/{age}/'
        return self.__year_data_from_endpoint(endpoint)

    def population_by_country_and_date(self, country, date):
        endpoint = f'/population/{country}/{date}/'
        return self.__date_data_from_endpoint(endpoint)

    def population_by_country_today_and_tomorrow(self, country):
        endpoint = f'/population/{country}/today-and-tomorrow/'
        return self.__date_data_from_endpoint(endpoint)

    def __year_data_from_endpoint(self, endpoint):
        raw_data = self.__fetch_endpoint(endpoint)
        return PopulationDataFactory().construct_year_data_list(raw_data)

    def __date_data_from_endpoint(self, endpoint):
        raw_data = self.__fetch_endpoint(endpoint)
        total_population_data = raw_data['total_population']

        ## HACK: for one endpoint, the data is a list, for the other it's a single JSON object.
        ## It's safe enough to go ahead and just foce the single object to be in a list
        if (type(total_population_data) is not list):
            total_population_data = [total_population_data]
        return PopulationDataFactory().construct_date_data_list(total_population_data)

    def __fetch_endpoint(self, endpoint):
        full_url = requote_uri(self.base_url + endpoint)
        binary_data = urllib.request.urlopen(full_url).read()
        text_data = binary_data.decode('utf-8')
        return json.loads(text_data)