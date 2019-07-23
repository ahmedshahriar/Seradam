import json
import pprint
import os
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['project2']
# db.drop()
ryans_collection = db['webs_ryans']
startech_collection = db['webs_startech']
mapping_collection = db['webs_mapping']
#
# brands = ['acer','apple','asus','chuwi','dell','hp','ilife','lenovo','microsoft','msi']
#
ryans_collection.drop()
startech_collection.drop()
mapping_collection.drop()

