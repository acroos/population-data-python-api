from year_population_data import YearPopulationData
from date_population_data import DatePopulationData

class PopulationDataFactory:
    def construct_year_data_list(self, raw_data):
        data_list = []
        for raw_year_data in raw_data:
            data_list.append(self.__construct_year_data(raw_year_data))
        
        return data_list

    def construct_date_data_list(self, raw_data):
        data_list = []
        for raw_date_data in raw_data:
            data_list.append(self.__construct_date_data(raw_date_data))

        return data_list

    def __construct_year_data(self, raw_data):
        return YearPopulationData(
            raw_data['country'],
            raw_data['age'],
            raw_data['females'],
            raw_data['males'],
            raw_data['total'],
            raw_data['year'])

    def __construct_date_data(self, raw_data):
        return DatePopulationData(raw_data['date'], raw_data['population'])