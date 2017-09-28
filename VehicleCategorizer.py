# python implementation of creating a webscraper to collect data from multiple websites on electric vehicles
# specs including battery capacity, make, model, year, retail locations
# possible setup of having a nested dictionaries that will append entries as it scrapes data from websites

# vehicle API website
# http://developer.edmunds.com/api-documentation/vehicle/
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
    def __init__(self):
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
        self.successCounter=0
        self.failureCounter=0
        
        # get the url of edmunds
        #self.edmunds_url = "https://www.topspeed.com/cars/plugin-cars/ke4486.html"
        # open the html file of the webpage
        #self.edmundsClient = uReq.get(self.edmunds_url)
        # get the webpage's html information
        #self.edmunds_soup = soup(self.edmundsClient.content)
        
        # get url for plugincars
        self.plugincars_url = "http://www.plugincars.com"
        self.plugincars_base_url = "http://www.plugincars.com/cars"
        # get contents of plugincars.com
        self.plugincarsClient = uReq.get(self.plugincars_base_url)
        # get webpage html contents
        # need the html.parser to get all of the information from this specific page
        self.plugincars_soup = soup(self.plugincarsClient.content, 'html.parser')
        # list to contain all of the urls scraped from the main plugincars page
        self.plugincars_url_list = []
        self.plugincars_car_names_list = []
        # plugincars divides up the individual cars into dividers with a mutual class of car-a
        # that being said, the names of each car is found under h3's text
        # print("got to the loop")
        for div in self.plugincars_soup.findAll("div", {"class" : "car-a"}):
            # get href to get the partial url to see the full details of each vehicle
            self.plugincars_url_list.append(self.plugincars_url+div.h3.a['href'])
            self.plugincars_car_names_list.append(div.h3.a.text)
        # plugincars urls are used to create their individual soups so that they can be parsed
        for i in range(len(self.plugincars_url_list)):
            # need to form a new client in order to get the soup from each url and then
            curr_plugincars_client = uReq.get(self.plugincars_url_list[i])
            # need to get the form the soup to scrape from the individual urls
            curr_plugincars_soup  = soup(curr_plugincars_client.content, "html.parser")
            # start sorintg out each of the pieces of information from the main soup
            # and individual car soup
            self.plugincars_dict[self.plugincars_car_names_list[i]]['make'] = curr_plugincars_soup.find("h3", {"class" : "vehicle-stats-title"}).text[0:curr_plugincars_soup.find("h3", class_="vehicle-stats-title").text.find(" ")]
            self.plugincars_dict[self.plugincars_car_names_list[i]]['model'] = curr_plugincars_soup.find("h3", {"class" : "vehicle-stats-title"}).text[curr_plugincars_soup.find("h3", class_="vehicle-stats-title").text.find(" ")+1:curr_plugincars_soup.find("h3", class_="vehicle-stats-title").text.find(" specifications")]
            self.plugincars_dict[self.plugincars_car_names_list[i]]['base_msrp($)'] = ''.join(x for x in curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[1].text if x.isdigit())
            self.plugincars_dict[self.plugincars_car_names_list[i]]['tech'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[3].text
            self.plugincars_dict[self.plugincars_car_names_list[i]]['body'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[4].text
            self.plugincars_dict[self.plugincars_car_names_list[i]]['range(mi)'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[6].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[6].text.find(" ")]
            self.plugincars_dict[self.plugincars_car_names_list[i]]['battery_capacity(kWh)'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[7].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[7].text.find(" ")] if curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[7].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[7].text.find(" ")] != '' else '-1'
            print("battery_cap", self.plugincars_dict[self.plugincars_car_names_list[i]]['battery_capacity(kWh)'])
            self.plugincars_dict[self.plugincars_car_names_list[i]]['charge_rate(kW)'] =curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[8].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[8].text.find(" ")] # if len(curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})) < 8 else " "
        
        
        # create csv file from the data collected
        
        fields =  ['car_name'] + list(list(self.plugincars_dict.values())[0].keys())
        with open('plugincars.csv','w', newline = '') as csvfile:
            writer = csv.DictWriter(csvfile, fields)
            writer.writeheader()
            for key in self.plugincars_dict:
                writer.writerow({field: self.plugincars_dict[key].get(field) or key for field in fields})
            csvfile.close()
                        
        #self.plugincars_page_soup = soup(self.plugincars_page_html, "html.parser")
        #must always have in order to add in new parameters to the class
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})

