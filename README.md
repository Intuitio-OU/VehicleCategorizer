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


- BeatifulSoup from bs4 library which is a fast and flexible parser for being able to access data from html and xml documents
- url open from urllib2/urllib to form client page
- html library from lxml allows python to access webpage (possibly won't use since BeautifulSoup and urlib may fulfill all necessary puposes)
- requests to extract text from webpages
- ratelimit library for constraining the scrape rate to prevent getting bloacked
- selenium library for web automation tools
- googlescraper is a custom python library from a github account that allows for the parsing of data in mutliple search engines including but limited to google
- xgoogle is tailored to google search engine specifically for web scraping
- scrapy is a web scraping library that can be implemented (need more details)

General consensus from multiple sites is that the main 2 libraries required are urllib/urllib2 and bs4 for the sake of urlopen and BeautifulSoup, yum soup :)

For those that are new to, WEB SCRAPING IS LEGAL for most websites so long as one does not scrape at alarming rates or violate an individual webpage's user agreement, have at it!

# References
https://www.quora.com/On-which-websites-can-I-do-web-scraping-legally
https://github.com/NikolaiT/GoogleScraper
https://elitedatascience.com/python-web-scraping-libraries
https://www.youtube.com/watch?v=XQgXKtPSzUI
https://github.com/DanielHabib/VenueCategorizer
https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
http://www.catonmat.net/blog/python-library-for-google-search/


