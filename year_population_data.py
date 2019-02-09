class YearPopulationData:
    def __init__(self, country, age, females, males, total, year):
        self.__country = country
        self.__age = age
        self.__females = females
        self.__males = males
        self.__total = total
        self.__year = year
    
    def fetch_country(self):
        return self.__country

    def fetch_age(self):
        return self.__age

    def fetch_female_population(self):
        return self.__females

    def fetch_male_population(self):
        return self.__males

    def fetch_total_population(self):
        return self.__total

    def fetch_year(self):
        return self.__year

    def __str__(self):
        return f"{{\n\tCountry: {self.__country},\n\tYear: {self.__year},\n\tAge: {self.__age},\n\tFemales: {self.__females},\n\tMales: {self.__males},\n\tTotal: {self.__total}\n}}"