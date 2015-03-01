#-------------------------------------------------------------------------------
# Name:        TSP_shareprices
# Author:      musashi
# Created:     28/02/2015
# Copyright:   (c) musashi 2015
#-------------------------------------------------------------------------------

import operator
import requests
from bs4 import BeautifulSoup

#TSP Shareprice website and input data
url = 'https://www.tsp.gov/investmentfunds/shareprice/sharePriceHistory.shtml'
post_data = {"startdate" : "02/25/2015",  "enddate":	"02/27/2015"}

#Submits POST data to website and gets website output
response = requests.post(url, data = post_data)

#Converts 'response' text to beautifulsoup format
soup = BeautifulSoup(response.text)

#Extracts the dates and shareprices
dates = soup.findAll(name='td', attrs={"class":"leadingCell"})
prices = soup.findAll(name="td",attrs={"class": "packed"})


#Writes to .csv file
with open('TSP_shareprices.csv', 'wb') as f:

    #Reversed loop for writing each date
    for count in range (0, len(dates)):

            #Converts dates to ascii format, cleans up format to be .csv compliant
            date = dates[count].contents[0].encode('ascii')
            date = date.replace(',', '')
            f.write(date)
            f.write(',')

            #Associates every 10 items to each date
            count2 = 0
            while prices:
                price = prices[0].contents[0].replace('\n', ',')
                f.write(price.encode('ascii'))
                prices.pop(0)
                count2 += 1
                if count2 == 10:
                   f.write('\n')
                   break
f.close()

##def sort_by_column(csv_cont, col, reverse=False):
##    """
##    Sorts CSV contents by column name (if col argument is type <str>)
##    or column index (if col argument is type <int>).
##
##    """
##    header = csv_cont[0]
##    body = csv_cont[1:]
##    if isinstance(col, str):
##        col_index = header.index(col)
##    else:
##        col_index = col
##    body = sorted(body,
##           key=operator.itemgetter(col_index),
##           reverse=reverse)
##    body.insert(0, header)
##    return body