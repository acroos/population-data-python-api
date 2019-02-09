class DatePopulationData:
    def __init__(self, date, population):
        self.__date = date
        self.__population = population

    def fetch_date(self):
        return self.__date

    def fetch_population(self):
        return self.__population

    def __str__(self):
        return f"{{\n\tDate: {self.__date},\n\tPopulation: {self.__population}\n}}"