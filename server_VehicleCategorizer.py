# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 17:47:54 2017

@author: mattanderson
"""
from VehicleCategorizer import VehicleCategorizer
from pymongo import MongoClient
from pprint import pprint

# mongodb connection string
connString = 'mongodb://mattandersoninf:Hummingbird95.@cluster0-shard-00-00-bzmsv.mongodb.net:27017,cluster0-shard-00-01-bzmsv.mongodb.net:27017,cluster0-shard-00-02-bzmsv.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

class VehicleCategorizerDatabase:
    # intitalize mongodb cluster connection
    def __init__(self):
        # create instance of VehicleCategorizer class
        self.vc = VehicleCategorizer()
        self.mongoClient = MongoClient(connString)
        self.plugincars_vehicles = self.plugincars_database['vehicles']
        
    # add data into the mognodb cluster based on which collection and database
    # must add data in json format
    def addData(self, database, collection, data, filename = None):
        if filename == None:
            self.monogoClient.vehicles.data.insert_one(data)
        else:
            # modify this condition to help add json formatted information into mongo cluster
            pass
            #self.mongoClient
            
    
    def deleteData(self, make, model, year):
        self.mongoClient.vehicles.data.delete_one()
    
    # return all vehicles in database with the make described    
    def getAllVehiclesByMake(self, make):
        self.mongoClient.vehicles.make
        
    # print all of the information for each vehicle in the plugincars database         
    def printAllVehiclesInPluginCarsDatabase(self):
        for vehicle in self.plugincars_vehicles.find():
            pprint(vehicle)
        print('Number of elements in the database:', len(list(self.plugincars_vehicles.find())))
