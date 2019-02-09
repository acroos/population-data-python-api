from api import Api

def main():
    population_api = Api()
    data = population_api.population(country='The Netherlands', age=28)
    
    print(data)

if __name__ == "__main__":
    # execute only if run as a script
    main()