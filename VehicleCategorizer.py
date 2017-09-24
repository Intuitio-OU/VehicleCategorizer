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
    self.plugincars_url = "http://www.plugincars.com/cars"
    
    # get contents of plugincars.com
    self.plugincarsClient = uReq.get(self.plugincars_url)
    
    # get webpage html contents
    # need the html.parser to get all of the information from this specific page
    self.plugincars_soup = soup(self.plugincarsClient.content, "html.parser")
    
    for atag in  self.plugincars_soup.find_all()
    
    # find a pattern for the car names, their all atags but you need to specify the dividers
    # that contain them uniquely
    
    
    #self.plugincars_page_soup = soup(self.plugincars_page_html, "html.parser")
    #must always have in order to add in new parameters to the class
    self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
    
# test grabbing information from the page
vc = VehicleCategorizer()
#for atag in vc.edmunds_soup.find_all("a"):
    #print(atag.text)
for a in vc.plugincars_soup.find_all("a"):
    print(a.text)    
#print(vc.plugincars_soup)    
    
