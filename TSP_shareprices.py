#-------------------------------------------------------------------------------
# Name:        TSP_shareprices
# Author:      musashi
# Created:     28/02/2015
# Copyright:   (c) musashi 2015
#-------------------------------------------------------------------------------

from bs4 import BeautifulSoup

import csv
import datetime
import operator
import requests
import sys

#TSP Shareprice website and input data
url = 'https://www.tsp.gov/investmentfunds/shareprice/sharePriceHistory.shtml'
post_data = {"startdate" : "01/01/2015",  "enddate":	"02/27/2015"}

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
            date = datetime.datetime.strptime(date, '%b %d %Y').strftime('%x')
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

#Load data from .csv file
data = csv.reader(open('TSP_shareprices.csv'), delimiter=',')

#Sort data
sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies according to first column we want to sort

#Write the sorted data result into .csv file
with open('TSP_shareprices.csv', 'wb') as f:
    fileWriter = csv.writer(f, delimiter=',')
    for row in sortedlist:
        fileWriter.writerow(row)
f.close()