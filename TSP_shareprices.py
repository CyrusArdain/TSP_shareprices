#-------------------------------------------------------------------------------
# Name:        TSP_shareprices
# Author:      musashi
# Created:     28/02/2015
# Copyright:   (c) musashi 2015
#-------------------------------------------------------------------------------

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
price = soup.findAll(name="td",attrs={"class": "packed"}, limit=10)


#Writes to .csv file
with open('TSP_shareprices.csv', 'wb') as f:

    #Loop for writing each date
    for count in range (0, len(dates)):

            #Converts stored data to ascii format, cleans up format to be .csv compliant
            date = dates[count].contents[0].encode('ascii')
            date = date.replace(',', '')
            f.write(date)
            f.write(',')

            #Loop for writing each fund price
            for count2 in range(0,len(price)):
                temp = price[count2].contents[0].replace('\n', ',')
                f.write(temp.encode('ascii'))
            f.write('\n')
f.close()