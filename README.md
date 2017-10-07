# VehicleCategorizer
----------------------------------------------------------------------------------------------------------------------------------------

Pull information from different websites about vehicles, need to specify the sites.

Information that is important to consider when looking at cars include mileage, safety rating, and mpg. This program is
specicifically tailored towards pulling infromation vehicles ranging from make, model, year, trim, base msrp, and mpg/ range.

Web scraping to be implemented on websites like google, google+, plugincars, jdpower, and edmunds.
Possible expansions with googlescraper being able to access more search engines

- BeatifulSoup from bs4: a fast and flexible parser for being able to access data from html and xml documents (this is probably what's going to be doing most of the heav lifting)
- requests: extract text from webpages
- ratelimit: library for constraining the scrape rate to prevent getting bloacked
- unittest: testing library
- time: track run time of all functions implemented
- tests currenlty demonstrate the ablility to generate urls for from the plugincars and edmunds sites and can extract a dataset from
  the plugincars site, scraping and generating urls for other sites are still in progress

General consensus from multiple sites is that the main 2 libraries required are requests and bs4.

# References
http://developer.edmunds.com/api-documentation/vehicle/
https://www.quora.com/On-which-websites-can-I-do-web-scraping-legally
https://github.com/NikolaiT/GoogleScraper
https://elitedatascience.com/python-web-scraping-libraries
https://www.youtube.com/watch?v=XQgXKtPSzUI
https://github.com/DanielHabib/VenueCategorizer
https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
http://www.catonmat.net/blog/python-library-for-google-search/

