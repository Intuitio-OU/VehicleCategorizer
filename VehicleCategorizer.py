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
from bs4 import SoupStrainer as strain
import requests as uReq
import grequests as gReq
from pprint import pprint
import csv
import time
import json
import re

class VehicleCategorizer:
    def __init__(self, maxFail = 10):
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
        self.edmunds_dict=collections.defaultdict(dict)
        # get connections to the databases of each site that was scraped
        #self.edmundsDB = self.mongoClient['edmundsDatabase']
        
        
        # counters for successful hits and failures
        
        # get the url of edmunds
        #self.edmunds_url = "https://www.topspeed.com/cars/plugin-cars/ke4486.html"
        # open the html file of the webpage
        #self.edmundsClient = uReq.get(self.edmunds_url)
        # get the webpage's html information
        #self.edmunds_soup = soup(self.edmundsClient.content)
        
        self.maxFail = maxFail
        self.failCounter = 0
        #self.plugincars_page_soup = soup(self.plugincars_page_html, "html.parser")
        #must always have in order to add in new parameters to the class
        self.__dict__.update({x:k for x, k in locals().items() if x != 'self'})
        
    def __repr__(self):
        return 'Vehicle Categroizer(maxFail=%s)'%(self.maxFail)
    def __str__(self):
        return str(self)
    
    # get all of the urls that you;re going to be scraping that are associated with
    # plugincars    
    def makePlugincarsUrlList(self):
        # get urls for plugincars, base url is for scraping the urls of each individual car webpage
        # and the other url is for appeniding the url of individual car page
        self.__initTry__()
        self.plugincars_url = "http://www.plugincars.com"
        self.plugincars_base_url = "http://www.plugincars.com/cars"
        # list to contain all of the urls scraped from the main plugincars page
        self.plugincars_url_list = []
        self.plugincars_car_names_list = []
        
        while True:
            try:
                # get contents of plugincars.com
                self.plugincarsClient = uReq.get(self.plugincars_base_url)
                soupStrain = strain('div',{"class" : "car-a"})
                # get webpage html contents
                # need the html.parser to get all of the information from this specific page
                self.plugincars_soup = soup(self.plugincarsClient.content, 'html.parser', parse_only = soupStrain)
                # plugincars divides up the individual cars into dividers with a mutual class of car-a
                # that being said, the names of each car is found under h3's text
                for div in list(self.plugincars_soup):
                    # get href to get the partial url to see the full details of each vehicle
                    self.plugincars_url_list.append(self.plugincars_url+div.h3.a['href'])
                    self.plugincars_car_names_list.append(div.h3.a.text)
                break
            # raise awareness if there's an issue connecting to the site
            except uReq.exceptions.TooManyRedirects:
                self.failCounter += 1
                print("There's an issue with connecting to plugincars.com")
            # if there are any issues that haven;t been accounted for, print it
            except uReq.exceptions.RequestException as e:
                self.failCounter += 1
                print("Unforseen error:",e)
            # you can keep trying to connect to the site, but if you've exceeded the maxFail count,
            # break the loop and display that there's an issue with makePlugincarsUrlList
            if self.failCounter == self.maxRequests:
                print('makePlugincarsUrlList error\n')
                break
            
    # get all of the information from the plugincars site
    # while scraping, if a cell returns -1, it means that the information
    # for this specific section was blank    
    def scrapePlugincars(self, filepath = 'plugincars.csv'):
        self.__initTry__()
        self.makePlugincarsUrlList()
        while True:
            try:
                rs = (gReq.get(url) for url in self.plugincars_url_list)
                r = list(gReq.map(rs))
                for response in r:
                    curr_plugincars_soup = soup(response.text, "html.parser")
                    curr_car_dict = self.plugincars_dict[response.url]
                    curr_car_dict['name'] = curr_plugincars_soup.find('h1').a.text
                    curr_car_dict['make'] = curr_plugincars_soup.find("h3", {"class" : "vehicle-stats-title"}).text[0:curr_plugincars_soup.find("h3", class_="vehicle-stats-title").text.find(" ")]
                    curr_car_dict['model'] = curr_plugincars_soup.find("h3", {"class" : "vehicle-stats-title"}).text[curr_plugincars_soup.find("h3", class_="vehicle-stats-title").text.find(" ")+1:curr_plugincars_soup.find("h3", class_="vehicle-stats-title").text.find(" specifications")]
                    curr_car_dict['base_msrp($)'] = ''.join(x for x in curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[1].text if x.isdigit()) if curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[1].text != '' else '-1'
                    curr_car_dict['tech'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[3].text
                    curr_car_dict['body'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[4].text
                    curr_car_dict['range(mi)'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[6].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[6].text.find(" ")]
                    curr_car_dict['battery_capacity(kWh)'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[7].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[7].text.find(" ")] if curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[7].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[7].text.find(" ")] != '' else '-1'
                    curr_car_dict['charge_rate(kW)'] = curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[8].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[8].text.find(" ")] if curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[8].text[0:curr_plugincars_soup.find_all("td", {"class" : "vehicle-stats-data"})[8].text.find(" ")] != '' else "-1"
                fieldnames = list(list(self.plugincars_dict.values())[0].keys())
                with open(filepath,'w', newline ='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames)
                    writer.writeheader()
                    for key in self.plugincars_dict: writer.writerow({field: self.plugincars_dict[key].get(field) or key for field in fieldnames})
                csvfile.close()
                break
            except uReq.exceptions.TooManyRedirects:
                self.failCounter += 1
                print("There's an issue with connecting to plugincars.com")
            except uReq.exceptions.RequestException as e:
                self.failCounter += 1
                print("Unforseen error:",e)
            except KeyError or AttributeError:
                self.failCounter += 1
                print("You're trying to grab an attribute that an xml element does not have.")
            except csv.Error:
                self.failCounter += 1
                print("There's problem when writing to the csv.")
            if self.failCounter == self.maxFail:
                print('scrapePluginCars error\n')
                break
    
    def printPlugincarsDict(self):
        pprint(dict(self.plugincars_dict))
    
    # create the urls so that you can use the requests function to scrape the edmunds site
    def makeEdmundsUrlList(self):
        self.edmunds_url = 'https://www.edmunds.com/'
        self.edmunds_url_set = set()
        self.edmunds_car_names_list = []
        self.__initTry__()
        #while True:
        #try:
        self.edmundsClient = uReq.get(self.edmunds_url)
        edmundsStrain = strain('a')
        edmundsSoup = list(soup(self.edmundsClient.content, 'html.parser', parse_only=edmundsStrain))[7:51]
        # this is the cleanest solution because it is possible that the site can add more car makes later but stable for extracting data in the mean time
        edmundsMakeRequests = (gReq.get(self.edmunds_url+a['href'][1:]) for a in edmundsSoup)
        edmundsMakeResponses = gReq.map(edmundsMakeRequests)
        for makeResponse in edmundsMakeResponses:
            print('made it to secondary loop with make response', makeResponse)
            if makeResponse == None: continue
            edmundsMakeStrain = strain('div',{'class' : "card-container"})
            edmundsMakeSoup = list(soup(makeResponse.text, 'html.parser', parse_only = edmundsMakeStrain))
            edmundsYearRS = (gReq.get(self.edmunds_url+div.a['href'][1:]) for div in edmundsMakeSoup)
            edmundsYearResponses = gReq.map(edmundsYearRS)
            for yearResponse in edmundsYearResponses:
                edmundsYearStrain = strain('li', {'class' : 'medium'})
                edmundsYearSoup = list(set(soup(yearResponse.text, 'html.parser', parse_only = edmundsYearStrain)))
                #pprint.pprint(edmundsYearSoup)
                for li in edmundsYearSoup:
                    #print('li_tYearSoup\n')
                    #print('li_tYearLink raw:', li.a['href'])
                    if li.a['href'].find('used/') != -1:
                        self.edmunds_url_set.add(self.edmunds_url+li.a['href'][1:])
                    else:
                        slCount = []
                        index = 0
                        while index < len(li.a['href']):
                            index = li.a['href'].find('/', index)
                            if index == -1:
                                break
                            slCount.append(index)
                            index += 1
                        if len(slCount) == 5 and (li.a['href'].find('review') == -1 and li.a['href'].find('features-specs') ==-1 and li.a['href'].find('consumer-reviews') and li.a['href'].find('deals') == -1):
                            self.edmunds_url_set.add(self.edmunds_url+li.a['href'][1:])
                        #break
            """
            except TypeError as e:
                print("You're hitting an object that is empty.")
                self.failCounter += 1
                if self.failCounter >= self.maxFail:
                    print("There is something wrong:", e)
            except Exception as e:
                self.failCounter += 1
                if self.failCounter >= self.maxFail:
                    print("There is something wrong:", e)
            """
    def printEdmundsUrlList(self):
        pprint(self.edmunds_url_set)
            
    def scrapeEdmunds(self):
        #scrape the details from each of the 
        edmundsResponseSet = (gReq.get(url) for url in self.edmunds_url_set)
        edmundsResponses = gReq.map(edmundsResponseSet)
        for response in edmundsResponses:
            self.edmunds_dict[response.url] = curr_edmunds_dict
            #curr_edmunds_dict 
    
        
    # reset the failCounter so that you keep attempting to scrape the site until you get a hit
    def __initTry__(self):
        self.failCounter = 0
       
"""
testReq = uReq.get('https://www.edmunds.com/aston-martin/')
testStrain = strain('div', {'class':'card-container'})
print(list(soup(testReq.content, 'html.parser', parse_only = testStrain))[0].a)
print('soup len', len(list(soup(testReq.content, 'html.parser', parse_only = testStrain))))
"""
