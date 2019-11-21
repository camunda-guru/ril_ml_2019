# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:07:45 2019

@author: Balasubramaniam
"""

from pymongo import MongoClient
#connect to the MongoDB.
conn = MongoClient('localhost',27017)
#Access the reliancedb database and the customer collection.
db = conn.reliancedb.customers
#document
customer_doc={
          "CustomerId":43567,
          "FirstName":"Roopa",
          "LastName":"Singh",
          "email":"roopa@gmail.com",
          "mobileNo":9988776688
        }

db.insert_one(customer_doc)
conn.close()






