#!/usr/bin/env python

# Import library for fetching Elspot data
from nordpool import elspot, elbas
from pprint import pprint
import json

# Initialize class for fetching Elspot prices
prices_spot = elspot.Prices()

# Initialize class for fetching Elsbas prices
prices_bas = elbas.Prices()

# Fetch hourly Elspot prices for Finland and print the resulting dictionary
#pprint(prices_spot.monthly(areas=['SE3']))
dict = prices_spot.monthly(areas=['SE3'])
list = dict['areas']['SE3']['values']
first, second, third, forth, *other = list
print(second['value'])
print(third['value'])
print(forth['value'])

average = (second['value']+third['value']+forth['value'])/3
print(average)

# Fetch hourly Elbas prices for Finland and print the resulting dictionary
#pprint(prices_bas.hourly(areas=['FI']))
