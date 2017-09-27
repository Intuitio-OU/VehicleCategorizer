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
        self.vc = VehicleCategorizer.VehicleCategorizer()
    
    
    # test the information scraped from the plugincars website    
    def test_plugincars(self):
        for i in range(len(self.vc.plugincars_car_names_list)):
            print("make:", self.vc.plugincars_dict[self.vc.plugincars_car_names_list[i]]['make'])
            print("model:", self.vc.plugincars_dict[self.vc.plugincars_car_names_list[i]]['model'])
            print("base_msrp($):", self.vc.plugincars_dict[self.vc.plugincars_car_names_list[i]]['base_msrp($)'])
            print("tech:", self.vc.plugincars_dict[self.vc.plugincars_car_names_list[i]]['tech'])
            print("body:",self.vc.plugincars_dict[self.vc.plugincars_car_names_list[i]]['body'])
            print("range(mi):", self.vc.plugincars_dict[self.vc.plugincars_car_names_list[i]]['range(mi)'])
            print("battery_capacity(kWh):", self.vc.plugincars_dict[self.vc.plugincars_car_names_list[i]]['battery_capacity(kWh)'])
            print("charge_rate(kW):", self.vc.plugincars_dict[self.vc.plugincars_car_names_list[i]]['charge_rate(kW)'])
    """
    def test_plugincars_csv(self):
        with open('plugincars.csv','r') as csvfile:
    """
            
# main function to run through all of the test function made in the test case
# use the middle arugrument argv=['first-arg-is-ignored'], exit = False because in ipy/ipynb files
# unittest.main looks at sys.argv first so you ignore argv so that unittest.main runs
if __name__ == '__main__':
    unittest.main()
