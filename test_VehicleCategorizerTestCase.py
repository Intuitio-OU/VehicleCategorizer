# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:35:52 2017

@author: mattanderson
"""

# get the vehivlecategorizer and unittest classes
import VehicleCategorizer
import unittest

# generate the testcase
class VehicleCategorizerTestCase(unittest.TestCase):
    # create a setup function
    def setUp(self):
        try: self.vCat = VehicleCategorizer.VehicleCategorizer()
        except ImportError as err:
            print("Are you even importing the correct class.")
     
    # test the information scraped from the plugincars website    
    def test_plugincars(self):
        try: self.vCat.scrapePlugincars('test_plugincars.csv')
        except KeyError as err: print("Check the dictionary keys")
        except IndexError: print("You're over indexing in the amount of variable that are available in the car name list.")
        
    """
    def test_plugincars_csv(self):
        with open('plugincars.csv','r') as csvfile:
    """
            
# main function to run through all of the test function made in the test case
# use the middle arugrument argv=['first-arg-is-ignored'], exit = False because in ipy/ipynb files
# unittest.main looks at sys.argv first so you ignore argv so that unittest.main runs
if __name__ == '__main__':
    unittest.main()
