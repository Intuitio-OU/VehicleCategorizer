
from lxml import html
import requests
from ratelimit import *
import requests
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen
import selenium
# DO RESEARCH ON THIS LIBRARY TO UNDERSTAND EXACTLY WHAT IT DOES 07-19-17, sounds useful refer to reseources
import scrapy
# in case you want to tap into googlescraper python library, use these lines
# import sys
# from GoogleScraper import scrape_with_config, GoogleSearchError
# from GoogleScraper.database import ScraperSearch, SERP, Link


class EVCategorizer:
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
    
  
  
  
  def __repr__(self):
		return "EV Category Scraper"
	def __iter__ (self):
		for a in urlList:
			yield a
	def __getitem__(self,key):
		for a in self.urlDict.keys():
			return urlDict[key]
	def __len__(self) :
		return len(entryList)
  
# set up retrieving the contents from each indvidual webpage
# EV google search webpage content, find another library, other possible solutions include xgoogle and json
googleEVSearchWebpage = request.get('https://www.google.com/#q=electric+vehicles')
googleSearchTree = html.fromstring(googleEVSearchWebpage.content)

# EV google plus search webpage content
googlePlusEVSearchWebpage = request.get('https://plus.google.com/+Cool-electric-cars')
googlePlusEVSearchTree = html.fromstring(googlePlusEVSearchWebpage.content)

# jdpower search webpage content
jdpowerSearchWebpage = request.get('https://plus.google.com/+Cool-electric-cars')
jdpowerSearchTree = html.fromstring(jdpowerSearchWebpage.content)

plugincarsUrl = raw_inputs("www.plugincars.com/cars")

plugincarsR = requests.get("http://"+plugincarsUrl)

plugincarsData = plugincarsR.text

#plugincarsContent = urllib2.urlopen(plugincarsUrl).read()

plugincarsSoup = BeautifulSoup(plugincarsData)

print plugincarsSoup.prettify()

print plugincarsSoup.title.string

#
