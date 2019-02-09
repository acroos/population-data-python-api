# population-data-python-api
Simple API wrapper for http://api.population.io/

## Usage

```
usage: main.py [-h] [--year YEAR] [--country COUNTRY] [--age AGE]
               [--date DATE]

Easily access population data from api.population.io

optional arguments:
  -h, --help         show this help message and exit
  --year YEAR        The year to get population data for (Cannot be used with
                     date)
  --country COUNTRY  The country to get population data for (if used alone,
                     will give data for today/tomorrow)
  --age AGE          The age to get population data for
  --date DATE        The date to get population data for (Can only be used
                     with country)

```