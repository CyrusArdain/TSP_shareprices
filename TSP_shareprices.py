#-------------------------------------------------------------------------------
# Name:        module1
# Author:      musashi
# Created:     28/02/2015
# Copyright:   (c) musashi 2015
#-------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup

url = 'https://www.tsp.gov/investmentfunds/shareprice/sharePriceHistory.shtml'
post_data = {"startdate" : "02/25/2015",  "enddate":	"02/27/2015"}

response = requests.post('''https://www.tsp.gov/investmentfunds/shareprice
                            /sharePriceHistory.shtml''', data = post_data)


