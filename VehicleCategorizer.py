# python implementation of creating a webscraper to collect data from multiple websites on electric vehicles
# specs including battery capacity, make, model, year, retail locations
# possible setup of having a nested dictionaries that will append entries as it scrapes data from websites

# vehicle API website
# http://developer.edmunds.com/api-documentation/vehicle/
# mainDict = websites
# mainDict.keys = {jdpower.com, google.com. googleplus, plugincars}
# mainDict.values ={[electricVehicle0Dict, electricVehicle1Dict.....]
# ex: electricVehicleDict0.keys = specifications mentioned above their corresponding values

from lxml import html
import requests
# this will be able to keep track of the data collection rate while scraping
from ratelimit import *
import requests
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen as uReq
import selenium
# DO RESEARCH ON THIS LIBRARY TO UNDERSTAND EXACTLY WHAT IT DOES 07-19-17, sounds useful refer to reseources
import scrapy
# in case you want to tap into googlescraper python library, use these lines
# import sys
# from GoogleScraper import scrape_with_config, GoogleSearchError
# from GoogleScraper.database import ScraperSearch, SERP, Link
# use this as reference for beautifulsoup4 class
# http://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python

class VehicleCategorizer:
  def _init_(self):
    # list container for URLs
    self.urlList=[]		
    # dict container for URLs
    self.urlDict= {}
    # dict containers for the URLs of each individual site
    # add more dictionaries if you wish to use googlescraper
    self.googleSearchUrlDict={}
    self.googlePlusUrlDict={}
    self.plugincarsUrlDict={}
    self.jdpowerUrlDict={}

    # counters for successful hits and failures
    self.successCounter=0
    self.failureCounter=0
    
    # start by webscraping for plugincars.com
    # website specific to electric vehicles
    plugincars_url = 'www.plugincars.com/cars'
    
