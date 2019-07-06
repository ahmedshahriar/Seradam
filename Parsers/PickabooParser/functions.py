from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

def get_smartphone_categories():
    html = urlopen("https://www.pickaboo.com/mobile-phone/smartphone.html")
    data = html.read()
    soup = BeautifulSoup(data, 'html.parser')
    categories = soup.findAll('div' , { "class": "submain-categ"} )
    smartphone_categories = []
    for category in categories:
        smartphone_categories.append(category.a['title'].lower())

    return  smartphone_categories



def get_featurephone_categories():
    html = urlopen("https://www.pickaboo.com/mobile-phone/feature-phone.html")
    data = html.read()
    soup = BeautifulSoup(data, 'html.parser')
    categories = soup.findAll('p' , { "class": "main-parent-category"} )
    featurephone_categories = []
    for category in categories:
        featurephone_categories.append(category.a['title'].lower())

    return  featurephone_categories



def get_smartphone_list(category):
    url = "https://www.pickaboo.com/mobile-phone/smartphone/" + category + ".html"

    json_file = "SmartPhone_" + category + "_list.json"
    write_file = open(json_file, 'w')

    total_products = []
    while url:
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        #print("url : " + url)
        products = soup.find_all('h2', {'class': 'product-name newname'});
        for product in products:
            product_url = product.a['href']
            title = product.a.string
            #print(title)
            product_records = {
                "product_title": title,
                "product_link": product_url
            }
            total_products.append(product_records)
        #print("loop ses")
        url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})
        #print("url : ", end="")
        #print(url)
        if url:
            url = url.get('href')
        else:
            break
    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()



def get_featurephone_list(category):
    url = "https://www.pickaboo.com/mobile-phone/feature-phone/" + category + ".html"

    json_file = "FeaturePhone_"+category+"_list.json"
    write_file = open(json_file, 'w')

    total_products = []
    while url:
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        #print("url : "+ url)
        products = soup.find_all('h2', {'class': 'product-name newname'});
        for product in products:
            product_url = product.a['href']
            title = product.a.string
            #print(title)
            product_records = {
                "product_title": title,
               "product_link": product_url
            }
            total_products.append(product_records)
        #print("loop ses")
        url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})
        #print("url : ",end="")
        #print(url)
        if url:
            url = url.get('href')
        else:
            break
    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()
