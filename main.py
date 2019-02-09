from api import Api
import argparse

population_api = Api()

def countries(args):
    countries_list = population_api.countries()
    print(",\n".join(countries_list))

def population(args):
    data = []
    ## Decide which api method should be called based on which parameters are passed in
    ## Be aggressive exiting if invalid combinations of args are passed
    if(args.year and not args.country and args.age and not args.date):
        data = population_api.population_by_year_and_age(args.year, args.age)
    elif(args.year and args.country and args.age and not args.date):
        data = population_api.population_by_year_country_and_age(args.year, args.country, args.age)
    elif(args.year and args.country and not args.age and not args.date):
        data = population_api.population_by_year_and_country(args.year, args.country)
    elif(not args.year and args.country and args.age and not args.date):
        data = population_api.population_by_country_and_age(args.country, args.age)
    elif(not args.year and args.country and not args.age and args.date):
        data = population_api.population_by_country_and_date(args.country, args.date)
    elif(not args.year and args.country and not args.age and not args.date):
        data = population_api.population_by_country_today_and_tomorrow(args.country)
    else:
        selected_args = []
        if args.year:
            selected_args.append('year')
        if args.country:
            selected_args.append('country')
        if args.age:
            selected_args.append('age')
        if args.date:
            selected_args.append('date')

        print(f'Invalid argument selection: [{", ".join(selected_args)}]')
        return
    
    print_data = ",\n".join(map(lambda x : str(x), data))
    print(print_data)

def main():
    parser = argparse.ArgumentParser(description='Simple CLI for api.population.io')

    subparsers = parser.add_subparsers(help='sub-command help', title='subcommands', description='')
    countries_subparser = subparsers.add_parser('countries', help='Retrieve a list of all available countries')
    countries_subparser.set_defaults(func=countries)

    population_data_subparser = subparsers.add_parser('population', help='Retrieve data about population for countries, years, ages, or dates')
    population_data_subparser.add_argument('--year', dest='year', help='The year to get population data for (Cannot be used with date)')
    population_data_subparser.add_argument('--country', dest='country', help='The country to get population data for (if used alone, will give data for today/tomorrow)')
    population_data_subparser.add_argument('--age', dest='age', help='The age to get population data for')
    population_data_subparser.add_argument('--date', dest='date', help='The date (yyyy-mm-dd) to get population data for (Can only be used with country). Valid dates are 2013-01-01 to 2022-12-31.')
    population_data_subparser.set_defaults(func=population)

    args = parser.parse_args()

    args.func(args)