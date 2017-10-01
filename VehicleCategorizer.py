# python implementation of creating a webscraper to collect data from multiple websites on electric vehicles
# specs including battery capacity, make, model, year, retail locations
# possible setup of having a nested dictionaries that will append entries as it scrapes data from websites

# mainDict = websites
# mainDict.keys = {jdpower.com, google.com. googleplus, plugincars}
# mainDict.values ={[electricVehicle0Dict, electricVehicle1Dict.....]
# ex: electricVehicleDict0.keys = specifications mentioned above their corresponding values

import collections
# from lxml import html
# this will be able to keep track of the data collection rate while scraping
# from ratelimit import *
from bs4 import BeautifulSoup as soup
import requests as uReq
import csv
import time
import multiprocessing
# learning curve for scrapy is a bit steeper and it is it's own api, bs4 more prefereable
# for the sake of developing you're own
# import scrapy

# in case you want to tap into googlescraper python library, use these lines
# import sys
# from GoogleScraper import scrape_with_config, GoogleSearchError
# from GoogleScraper.database import ScraperSearch, SERP, Link
# use this as reference for beautifulsoup4 class
# http://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python

class VehicleCategorizer:
    def __init__(self, maxScrapeAttempts = 10):
        # list container for URLs
        self.urlList=[]		
        # dict container for URLs
        self.urlDict= {}
        # dict containers for the URLs of each individual site
        # add more dictionaries if you wish to use googlescraper
        #self.googleSearchUrlDict={}
        #self.googlePlusUrlDict={}
        self.topspeedUrlDict={}
        #self.jdpowerUrlDict={}
        self.plugincars_dict=collections.defaultdict(dict)
        
        # counters for successful hits and failures
        self.successCounter = 0
        self.failureCounter = 0
        self.maxRequests = maxRequests
        
        # get the url of edmunds
        #self.edmunds_url = "https://www.topspeed.com/cars/plugin-cars/ke4486.html"
        # open the html file of the webpage
        #self.edmundsClient = uReq.get(self.edmunds_url)
        # get the webpage's html information
        #self.edmunds_soup = soup(self.edmundsClient.content)
        
        #self.plugincars_page_soup = soup(self.plugincars_page_html, "html.parser")
        #must always have in order to add in new parameters to the class
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
        
    def scrapePlugincars(self, filepath = 'plugincars.csv'):
        self.__initScrape__()
        # get urls for plugincars, base url is for scraping the urls of each individual car webpage
        # and the other url is for appeniding the url of individual car page
        plugincars_url = "http://www.plugincars.com"
        plugincars_base_url = "http://www.plugincars.com/cars"
        # get contents of plugincars.com
        while True:
            try:
                uReq.get(plugincars_base_url)
                
            except Exception as err:
                self.failureCounter += 1
                if self.failureCounter > self.maxRequests:
                    print('Requests failed for plugincars, check site or possibly drop requests rate.')
                    break
            else: break
            
        plugincarsClient = uReq.get(plugincars_base_url)
        # get webpage html contents
        # need the html.parser to get all of the information from this specific page
        while True:
            try:
                soup(plugincarsClient.content, 'html.parser')
            except Exception as err:
                self.failureCounter += 1
                if self.failureCounter > self.maxRequests:
                    print('Something is very wrong, refer to this',err)
                    break
            else: break
        plugincars_soup = soup(plugincarsClient.content, 'html.parser')
        # list to contain all of the urls scraped from the main plugincars page
        plugincars_url_list = []
        plugincars_car_names_list = []
        # plugincars divides up the individual cars into dividers with a mutual class of car-a
        # that being said, the names of each car is found under h3's text
        # print("got to the loop")
        for div in plugincars_soup.findAll("div", {"class" : "car-a"}):
            # get href to get the partial url to see the full details of each vehicle
            plugincars_url_list.append(plugincars_url+div.h3.a['href'])
            plugincars_car_names_list.append(div.h3.a.text)
        # plugincars urls are used to create their individual soups so that they can be parsed
        for i in range(len(plugincars_url_list)):
            # need to form a new client in order to get the soup from each url and then
            curr_plugincars_client = uReq.get(self.plugincars_url_list[i])
            # need to get the form the soup to scrape from the individual urls
            curr_plugincars_soup  = soup(curr_plugincars_client.content, "html.parser")
            # start sorintg out each of the pieces of information from the main soup
            # and individual car soup
            # there is an option to put the keys into the
            curr_car_dict = self.plugincars_dict[plugincars_car_names_list[i]]
            curr_car_dict['make'] = curr_plugincars_soup.find("h3", {"class" : "vehicle-stats-title"}).text[0:curr_plugincars_soup.find("h3", class_="vehicle-stats-title").text.find(" ")]
            curr_car_dict['model'] = curr_plugincars_soup.find("h3", {"class" : "vehicle-stats-title"}).text[curr_plugincars_soup.find("h3", class_="vehicle-stats-title").text.find(" ")+1:curr_plugincars_soup.find("h3", class_="vehicle-stats-title").text.find(" specifications")]
            curr_car_dict['base_msrp($)'] = ''.join(x for x in curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[1].text if x.isdigit())
            curr_car_dict['tech'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[3].text
            curr_car_dict['body'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[4].text
            curr_car_dict['range(mi)'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[6].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[6].text.find(" ")]
            curr_car_dict['battery_capacity(kWh)'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[7].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[7].text.find(" ")] if curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[7].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[7].text.find(" ")] != '' else '-1'
            curr_car_dict['charge_rate(kW)'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[8].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[8].text.find(" ")] if curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[8].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[8].text.find(" ")] != '' else "-1"
                
        # create csv file from the data collected
        # intialize a list for the parameters that classify your values        
        fieldnames =  ['car_name'] + list(list(self.plugincars_dict.values())[0].keys())
        # write the collected information in the dictionary for plugincars into a csv file labeled plugincars.csv
        with open(filepath,'w', newline ='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()
            for key in self.plugincars_dict: writer.writerow({field: self.plugincars_dict[key].get(field) or key for field in fieldnames})
        csvfile.close()
        
    
    def __initScrape__(self):
        self.successCounter = 0
        self.failureCounter = 0
    