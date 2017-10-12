# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:35:52 2017

@author: mattanderson
"""

# get the vehivlecategorizer and unittest classes
import VehicleCategorizer
import unittest
import time

# generate the testcase
class VehicleCategorizerTestCase(unittest.TestCase):
    # create a setup function
    def setUp(self):
        try:
            self.vCat = VehicleCategorizer.VehicleCategorizer()
        except ImportError as err: print("Check that you imported the VehicleCategorizer class and that it's in the same folder as this test script.")
     
    # test the information scraped from the plugincars website    
    @unittest.skip("Skip plugincars for this test.")
    def test_plugincars(self):
        try:
            start = time.time()
            self.vCat.scrapePlugincars('test_plugincars.csv')
            end = time.time()
            # print the information collected during the test so that I can
            # manually check the information
            self.vCat.printAllVehiclesInPluginCarsDatabase()
            #pprint(list(self.vCat.plugincars_dict.values()))
            print('\nScrapePlugincars exec time: %.2fs\n'%(end-start))
        except KeyError as err: print("Check the dictionary keys")
        except IndexError: print("You're over indexing in the amount of variable that are available in the car name list.")
     
    # test the information collected from the edmunds site (still in progress)
    #@unittest.skip("Skip edmunds for this test.")
    def test_edmunds(self):
        try:
            start = time.time()
            self.vCat.makeEdmundsUrlList()
            end = time.time()
            print('\nMake Edmunds Url List exec time: %.2fs\n'%(end-start))
        except Exception as e:
            print(e)
    """
    def test_plugincars_csv(self):
        with open('plugincars.csv','r') as csvfile:
    """
            
# main function to run through all of the test function made in the test case
# use the middle arugrument argv=['first-arg-is-ignored'], exit = False because in ipy/ipynb files
# unittest.main looks at sys.argv first so you ignore argv so that unittest.main runs
if __name__ == '__main__':
    unittest.main()
