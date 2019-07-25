import json
import pprint
import os
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['project-test']
ryans_collection = db['webs_ryans']
startech_collection = db['webs_startech']
mapping_collection = db['webs_mapping']

brands = ['Acer', 'Apple', 'Asus', 'Chuwi', 'Dell', 'HP', 'iLife', 'Lenovo', 'Microsoft', 'MSI']

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

ryans_path = "./json/ryans/laptop/Fujitsu.json"

startech_path = "./json/startech/laptop/Razer.json"

ryans_product_list = json.loads(open(ryans_path).read())['Products']
startech_product_list = json.loads(open(startech_path).read())['Products']

ryans_collection.insert_many(
    ryans_product_list
)
startech_collection.insert_many(
    startech_product_list
)


ryans = ryans_collection.find()
flag = 0
for r in ryans:

    model = r['model']+" "
    startech = startech_collection.find()
    flag = 0
    for s in startech:
        if model in s['product_title']:
            # print(r['product_link'])
            # print(s['product_link'])
            r_display = r['display_size'][:-1]
            s_display = s['display_size'][:-1]

            flag += 1
            mapping_collection.insert_one({
                "ryans": r['_id'],
                "startech": s['_id']
            })

    # print("1 to {} relation".format(flag))


