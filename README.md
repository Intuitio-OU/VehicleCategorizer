# EVCategorizer

Pull information from different websites about specific electric vehicles.

Information that is important to consider when looking at cars include mileage, safety rating, and mpg. This program is
specicifically tailored towards pulling infromation about electric vehicles like battery capacity, safety rating, model
brand/manufaturer, price(leasing and buying), heating, ac, mileage (new or used), year, space, type (sedan, suv), etc. Electric cars in particular.

Web scraping to be implemented on websites like google, google+, plugincars, and jdpower.
Possible expansions with googlescraper being able to access more search engines

There are pros and cons to using some libraries so rather than scower the internet for information on each library,
here are the purposes and pros and cons of each used library (some libraries may not be used by the end but
keep out of convenience of knowledge)

html library from lxml allows 

# use repl.it for compiling
# http library that allows python to access webpages, easy and fast xml and html library in python, same as soup 4 but easier and faster to pick up
# ideal for static webpages
from lxml import html
import requests
# WEB SCRAPING IS LEGAL for most websites
# so long as one does not scrape at alarming rates or violate an individual webpage's user agreement, have at it!
# https://www.quora.com/On-which-websites-can-I-do-web-scraping-legally
# should help with rate limiting
from ratelimit import *
import requests
# allows you to analyze the contents of the page (python parsing library), specifically for messy sites
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen
# web automation library, open up the browser and navigate to desired pages
import selenium
# DO RESEARCH ON THIS LIBRARY TO UNDERSTAND EXACTLY WHAT IT DOES 07-19-17, sounds useful refer to reseources
import scrapy
# in case you want to tap into googlescraper python library, use these lines
# import sys
# from GoogleScraper import scrape_with_config, GoogleSearchError
# from GoogleScraper.database import ScraperSearch, SERP, Link
# came from this github account
# https://github.com/NikolaiT/GoogleScraper
# scrapes google, bing, and other search engines
# however general consensus from multiple sites is that the main 2 libraries required are urllib/urllib2 and bs4
# for the sake of urlopen and BeautifulSoup, yum soup :)

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
# replace with bs4 library for google search scraping and jdpower
# be careul with rate limiting (the amount of requests that are allowed for a webpage)
