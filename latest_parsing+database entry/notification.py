from pymongo import MongoClient
import pymongo
from pprint import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client['project']
ryans_collection = db['products_ryans']
startech_collection = db['products_startech']
wishlist_collection = db['wishlist_wishlist']
notification_collection = db['products_notification']



wishlists = wishlist_collection.find()
ryans = ryans_collection.find()
startech = startech_collection.find()


data = notification_collection.find({},{'id':1}).sort('id', -1).limit(1)

if data.count() == 0:
    id = 1
else:
    id = data[0]['id']+1

for wishlist in wishlists:
    user_id = wishlist['user_id']
    product_title = wishlist['product_title']
    # print("userid : "+str(user_id))
    # print("product_title : "+product_title)

    for website in wishlist['websites']:
        website_name = website['website_name']
        wishlist_price = website['price']
        product_link = website['product_link']

        # print(wishlist_price)
        if website_name == "ryanscomputers.com":
            data = ryans_collection.find({"product_link" : product_link},{"price": 1})

            # print("printing data")
            if data.count()> 0:
                if wishlist_price != data[0]['price']:
                    print("change found")
                    notification_collection.insert_one({
                        "id": id,
                        "user_id" : user_id,
                        "product_title" : product_title,
                        "product_link" : product_link,
                        "website_name" : website_name,
                        "old_price" : wishlist_price,
                        "new_price" : data[0]['price'],
                        "seen": False
                    })
                    id += 1

            # if(data)

        # if website['website_name'] == 'ryanscomputers.com':


    print()
    print()