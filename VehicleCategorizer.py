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
#from lxml import html
# this will be able to keep track of the data collection rate while scraping
# from ratelimit import *
# import bs4
from bs4 import BeautifulSoup as soup
import requests as uReq
#import selenium
# DO RESEARCH ON THIS LIBRARY TO UNDERSTAND EXACTLY WHAT IT DOES 07-19-17, sounds useful refer to reseources

# learning curve for scrapy is a bit steeper and it is it's own api, bs4 more prefereable
# for the sake of developing you're own
#import scrapy

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
        self.plugincars_url_dict=collections.defaultdict(dict)
        
        # counters for successful hits and failures
        self.successCounter=0
        self.failureCounter=0
        
        # get the url of edmunds
        self.edmunds_url = "https://www.topspeed.com/cars/plugin-cars/ke4486.html"
        # open the html file of the webpage
        self.edmundsClient = uReq.get(self.edmunds_url)
        # get the webpage's html information
        self.edmunds_soup = soup(self.edmundsClient.content)
        
        # get url for plugincars
        self.plugincars_base_url = "http://www.plugincars.com/cars"
        
        # get contents of plugincars.com
        self.plugincarsClient = uReq.get(self.plugincars_base_url)
        
        # get webpage html contents
        # need the html.parser to get all of the information from this specific page
        self.plugincars_soup = soup(self.plugincarsClient.content, "html.parser")
        
        self.plugincars_url_list = []
        # plugincars divides up the individual cars into dividers with a mutual class of car-a
        # that being said, the names of each car is found under h3's text
        for div in self.plugincars_soup.find_all("div", class_="car-a"):
            # get href to get the partial url to see the full details of each vehicle
            self.plugincars_url_list.append(self.plugincars_base_url+str(div.h3.a['href']))
        for url in self.plugincars_url_list:
            # need to form a new client in order to get the soup from each url and then
            curr_plugincars_client = uReq.get(url)
            # need to get the form the soup to scrape from the individual urls
            curr_plugincars_soup  = soup(curr_plugincars_client.content, "html.parser")
            
            #self.plugincars_url_dict[url]
        
        #self.plugincars_page_soup = soup(self.plugincars_page_html, "html.parser")
        #must always have in order to add in new parameters to the class
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})

    def get_plugincars_names(self):
        return self.plugincars_names
    
        
        
# test grabbing information from the page
vc = VehicleCategorizer()
#for atag in vc.edmunds_soup.find_all("a"):
    #print(atag.text)
for i in vc.plugincars_url_list:
    print(i)
#print(vc.plugincars_soup)    
    
