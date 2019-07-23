import json
import pprint
import os
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['project2']
ryans_collection = db['webs_ryans']
startech_collection = db['webs_startech']
mapping_collection = db['webs_mapping']

brands = ['acer','apple','asus','chuwi','dell','hp','ilife','lenovo','microsoft','msi']

ryans_collection.drop()
startech_collection.drop()
mapping_collection.drop()


for brand in brands:
    ryans_path = "./json/ryans/laptop/"+brand+".json"
    startech_path = "./json/startech/laptop/"+brand+".json"

    ryans_product_list = json.loads(open(ryans_path).read())['Products']
    startech_product_list = json.loads(open(startech_path).read())['Products']

    ryans_collection.insert_many(
        ryans_product_list
    )
    startech_collection.insert_many(
        startech_product_list
    )

ryans_path = "./json/ryans/laptop/fujitsu.json"

startech_path = "./json/startech/laptop/razer.json"

ryans_product_list = json.loads(open(ryans_path).read())['Products']
startech_product_list = json.loads(open(startech_path).read())['Products']

ryans_collection.insert_many(
    ryans_product_list
)
startech_collection.insert_many(
    startech_product_list
)



products = ryans_collection.find()
flag = 0
for product in products:

    model = product['model']+" "
    temp = startech_collection.find()
    flag=0
    for t in temp:
        if model in t['product_title']:
            flag+=1
            mapping_collection.insert_one({
                "ryans": product['_id'],
                "startech": t['_id']
            })


    # if flag > 0: print("1 to {} relation".format(flag))



# ryans_collection.drop()
# startech_collection.drop()
# mapping_collection.drop()
