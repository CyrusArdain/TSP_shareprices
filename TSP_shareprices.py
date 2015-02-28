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

response = requests.post(url, data = post_data)

soup = BeautifulSoup(response.text)

dates = soup.findAll(name='td', attrs={"class":"leadingCell"})
price = soup.findAll(name="td",attrs={"class": "packed"}, limit=10)

with open('test2.csv', 'a') as f:
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