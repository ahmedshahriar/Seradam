import json
import pprint
import os
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['project2']
startech_collection = db['webs_startech']

brands = ['acer','apple','asus','chuwi','dell','hp','ilife','lenovo','microsoft','msi']

# ryans_collection.drop()
startech_collection.drop()
# mapping_collection.drop()


for brand in brands:
    startech_path = "./json/startech/laptop/"+brand+".json"

    startech_product_list = json.loads(open(startech_path).read())['Products']

    startech_collection.insert_many(
        startech_product_list
    )


startech_path = "./json/startech/laptop/razer.json"

startech_product_list = json.loads(open(startech_path).read())['Products']

startech_collection.insert_many(
    startech_product_list
)






# ryans_collection.drop()
# startech_collection.drop()
# mapping_collection.drop()
