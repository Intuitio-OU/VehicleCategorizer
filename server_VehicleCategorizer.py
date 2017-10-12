# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 17:47:54 2017

@author: mattanderson
"""
from VehicleCategorizer import VehicleCategorizer
from pymongo import MongoClient
from pymongo import ReturnDocument
from pprint import pprint

class VehicleCategorizerDatabase:
    def __init__(self):
        self.vc = VehicleCategorizer()
        self.mongoClient = MongoClient('localhost', 27017)
        self.plugincars_database = self.mongoClient.plugincars_database
        #print('plugincars databse name:', self.plugincars_database.name)
        #print('plugincars databse:', self.plugincars_database)
        self.plugincars_vehicles = self.plugincars_database['vehicles']
        self.plugincars_vehicles.drop()
        print('vehicles database cleared')
        #self.plugincars_collection = self.plugincars_database['plugincars_collection']
        #print('plugincars collections',self.plugincars_database.collection_names)
        #self.plugincars_vehicles.insert_one(curr_car_dict)
        #print('collections in plugincars database:', self.plugincars_database.collection_names(include_system_collections=False))
            
    # print all of the information for each vehicle in the plugincars database         
    def printAllVehiclesInPluginCarsDatabase(self):
        for vehicle in self.plugincars_vehicles.find():
            pprint(vehicle)
        print('Number of elements in the database:', len(list(self.plugincars_vehicles.find())))
