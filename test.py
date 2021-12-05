#!/usr/bin/env python

# Import library for fetching Elspot data
from nordpool import elspot, elbas
from pprint import pprint

# Initialize class for fetching Elspot prices
prices_spot = elspot.Prices()

# Initialize class for fetching Elsbas prices
prices_bas = elbas.Prices()

# Fetch hourly Elspot prices for Finland and print the resulting dictionary
pprint(prices_spot.monthly(areas=['SE3'],end_date='2021-05-01',start_date='2021-01-01'))

# Fetch hourly Elbas prices for Finland and print the resulting dictionary
#pprint(prices_bas.hourly(areas=['FI']))
