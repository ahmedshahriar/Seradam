import json
import pprint
import os
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['project3']
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
    startech = startech_collection.find(
        {
            "brand": r['brand'],
            'ram': r['ram'],
            'graphics_memory': r['graphics_memory']
        })
    flag = 0
    print()
    print(r['product_link'])
    mapped = False
    for s in startech:

        if model in s['product_title']:
            # print(r['product_link'])
            print(s['product_link'])
            mapped = True
            flag += 1
            mapping_collection.insert_one({
                "brand" : r['brand'],
                "description" : r['description'],
                "display_size" : r['display_size'],
                "display_type" : r['display_type'],
                "graphics_memory" : r['graphics_memory'],
                "img_link" : r['img_link'],
                "model" : r['model'],
                "product_title" : r['product_title'],
                "ram" : r['ram'],
                "ram_type" : r['ram_type'],
                "storage" : r['storage'],
                "websites" : [
                    {
                        "website_name" : r['website'],
                        "price" : r['price'],
                        "product_link" : r['product_link'],
                        "status" : r['status']
                    },
                    {
                        "website_name" : s['website'],
                        "price" : s['price'],
                        "product_link" : s['product_link'],
                        "status" : s['status']
                    }
                ]
                # _id = models.CharField(primary_key=True, max_length=100)

            })
    if not mapped:
        mapping_collection.insert_one({
            "brand": r['brand'],
            "description": r['description'],
            "display_size": r['display_size'],
            "display_type": r['display_type'],
            "graphics_memory": r['graphics_memory'],
            "img_link": r['img_link'],
            "model": r['model'],
            "product_title": s['product_title'],
            "ram": r['ram'],
            "ram_type": r['ram_type'],
            "storage": r['storage'],
            "websites": [
                {
                    "website_name": r['website'],
                    "price": r['price'],
                    "product_link": r['product_link'],
                    "status": r['status']
                }
            ]
            # _id = models.CharField(primary_key=True, max_length=100)

        })
    print("1 to {} relation".format(flag))


