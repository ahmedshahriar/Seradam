import json
import pprint
import os
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['project']
ryans_collection = db['products_ryans']
startech_collection = db['products_startech']
mapping_collection = db['products_mapping']

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

# ryans_path = "./json/ryans/laptop/Fujitsu.json"
# ryans_product_list = json.loads(open(ryans_path).read())['Products']
# ryans_collection.insert_many(
#     ryans_product_list
# )

startech_path = "./json/startech/laptop/Razer.json"
startech_product_list = json.loads(open(startech_path).read())['Products']
#

startech_collection.insert_many(
    startech_product_list
)


ryans = ryans_collection.find()
flag = 0
id = 1
for r in ryans:

    model = r['model']+" "
    startech = startech_collection.find(
        {
            "brand": r['brand'],
            'ram': r['ram'],
            'graphics_memory': r['graphics_memory'],
            'processor': r['processor'],
            'storage': r['storage']
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
                "id": id,
                "brand": r['brand'],
                "description": r['description'],
                "display_size": r['display_size'],
                "graphics_memory": r['graphics_memory'],
                "img_link": r['img_link'],
                "product_title": s['product_title'],
                "ram": r['ram'],
                "ram_type": r['ram_type'],
                "storage": r['storage'],
                "websites": [
                    {
                        "website_name": r['website'],
                        "price": r['price'],
                        "product_link": r['product_link'],
                        "status": r['status'],
                        "img_link": r['img_link']
                    },
                    {
                        "website_name": s['website'],
                        "price": s['price'],
                        "product_link": s['product_link'],
                        "status": s['status'],
                        "img_link": s['img_link']
                    }
                ]
                # _id = models.CharField(primary_key=True, max_length=100)

            })
            id = id+ 1
    if not mapped:
        mapping_collection.insert_one({
            "id": id,
            "brand": r['brand'],
            "description": r['description'],
            "display_size": r['display_size'],
            "graphics_memory": r['graphics_memory'],
            "img_link": r['img_link'],
            "product_title": r['product_title'],
            "ram": r['ram'],
            "ram_type": r['ram_type'],
            "storage": r['storage'],
            "websites": [
                {
                    "website_name": r['website'],
                    "price": r['price'],
                    "product_link": r['product_link'],
                    "status": r['status'],
                    "img_link": r['img_link']
                },
            ]
            # _id = models.CharField(primary_key=True, max_length=100)

        })
        id += 1
    print("1 to {} relation".format(flag))


