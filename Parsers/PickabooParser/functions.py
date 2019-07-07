from bs4 import BeautifulSoup
from urllib.request import urlopen
import json



def get_mobile_list():

    print("parsing mobiles")
    json_file = "./json/mobile_list.json"
    write_file = open(json_file, 'w')
    total_products = []

    url = "https://www.pickaboo.com/mobile-phone/smartphone.html"
    while url:
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'product-item'})
        i = 0
        for product in products:

            product_url = product.h2.a['href']
            title = product.h2.a.string.strip()

            img_link = product.a.img['data-original']

            price = soup.find_all(attrs={"itemprop": "price"})[i]

            i = i+1
            price = price.text
            price = str(price).replace('৳', '')
            price = str(price).replace(',', '').strip()

            if product.find('div', {'class': 'bottom syn-soldout'}):
                status = "not available"
            else:
                status = "available"

            product_records = {
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title
            }
            total_products.append(product_records)

        url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})

        if url:
            url = url.get('href')
        else:
            break
    #json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))

    print("smart phone done")


    url = "https://www.pickaboo.com/mobile-phone/feature-phone.html"
    while url:
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'product-item'})
        i = 0
        for product in products:

            product_url = product.h2.a['href']
            title = product.h2.a.string.strip()
            img_link = product.a.img['data-original']

            price = soup.find_all(attrs={"itemprop": "price"})[i]

            i = i + 1
            price = price.text
            price = str(price).replace('৳', '')
            price = str(price).replace(',', '').strip()

            if product.find('div', {'class': 'bottom syn-soldout'}):
                status = "not available"
            else:
                status = "available"

            product_records = {
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title
            }
            total_products.append(product_records)

        url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})

        if url:
            url = url.get('href')
        else:
            break
    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))

    print("feature phone done")
    write_file.close()





def get_mobileAccessories_list():

    print("parsing mobile accessories")
    json_file = "./json/mobileAccessories_list.json"
    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    url = "https://www.pickaboo.com/mobile-accessories.html/"
    while url:
        print(page)
        page +=1

        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'product-item'})
        i = 0
        for product in products:

            product_url = product.h2.a['href']
            title = product.h2.a.string.strip()

            img_link = product.a.img['data-original']

            price = soup.find_all(attrs={"itemprop": "price"})[i]

            i = i+1
            price = price.text
            price = str(price).replace('৳', '')
            price = str(price).replace(',', '').strip()

            if product.find('div', {'class': 'bottom syn-soldout'}):
                status = "not available"
            else:
                status = "available"

            product_records = {
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title
            }
            total_products.append(product_records)

        url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})

        if url:
            url = url.get('href')
        else:
            break

    print("mobile accessories done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))


    write_file.close()





def get_computer_list():

    print("parsing computers")
    json_file = "./json/computer_list.json"
    write_file = open(json_file, 'w')
    total_products = []

    url = "https://www.pickaboo.com/computer-pc/laptop-notebook.html/"
    while url:
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'product-item'})
        i = 0
        for product in products:

            product_url = product.h2.a['href']
            title = product.h2.a.string.strip()

            img_link = product.a.img['data-original']

            price = soup.find_all(attrs={"itemprop": "price"})[i]

            i = i+1
            price = price.text
            price = str(price).replace('৳', '')
            price = str(price).replace(',', '').strip()

            if product.find('div', {'class': 'bottom syn-soldout'}):
                status = "not available"
            else:
                status = "available"

            product_records = {
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title
            }
            total_products.append(product_records)

        url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})

        if url:
            url = url.get('href')
        else:
            break
    #json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))

    print("laptop done")


    url = "https://www.pickaboo.com/computer-pc/desktop-computer.html"
    while url:
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'product-item'})
        i = 0
        for product in products:

            product_url = product.h2.a['href']
            title = product.h2.a.string.strip()

            img_link = product.a.img['data-original']

            price = soup.find_all(attrs={"itemprop": "price"})[i]

            i = i+1
            price = price.text
            price = str(price).replace('৳', '')
            price = str(price).replace(',', '').strip()

            if product.find('div', {'class': 'bottom syn-soldout'}):
                status = "not available"
            else:
                status = "available"

            product_records = {
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title
            }
            total_products.append(product_records)

        url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})

        if url:
            url = url.get('href')
        else:
            break

    print("desktop done")



    url = "https://www.pickaboo.com/computer-pc/tablet.html/"

    while url:
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'product-item'})
        i = 0
        for product in products:

            product_url = product.h2.a['href']
            title = product.h2.a.string.strip()

            img_link = product.a.img['data-original']

            price = soup.find_all(attrs={"itemprop": "price"})[i]

            i = i+1
            price = price.text
            price = str(price).replace('৳', '')
            price = str(price).replace(',', '').strip()

            if product.find('div', {'class': 'bottom syn-soldout'}):
                status = "not available"
            else:
                status = "available"

            product_records = {
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title
            }
            total_products.append(product_records)

        url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})

        if url:
            url = url.get('href')
        else:
            break

    print("tablet done")


    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))

    write_file.close()





def get_computerAccessories_list():


    print("computer accessories")
    json_file = "./json/computerAccessories_list.json"
    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    url = "https://www.pickaboo.com/computer-pc/computer-accessories.html/"
    while url:
        print(page)
        page +=1

        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'product-item'})
        i = 0
        for product in products:

            product_url = product.h2.a['href']
            title = product.h2.a.string.strip()

            img_link = product.a.img['data-original']

            price = soup.find_all(attrs={"itemprop": "price"})[i]

            i = i+1
            price = price.text
            price = str(price).replace('৳', '')
            price = str(price).replace(',', '').strip()

            if product.find('div', {'class': 'bottom syn-soldout'}):
                status = "not available"
            else:
                status = "available"

            product_records = {
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title
            }
            total_products.append(product_records)

        url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})

        if url:
            url = url.get('href')
        else:
            break

    print("computer accessories done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))


    write_file.close()





def get_gaming_console_list():


    print("gaming console")
    json_file = "./json/gaming_console_list.json"
    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    url = "https://www.pickaboo.com/computer-pc/gaming-console.html/"
    while url:
        print(page)
        page +=1

        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'product-item'})
        i = 0
        for product in products:

            product_url = product.h2.a['href']
            title = product.h2.a.string.strip()

            img_link = product.a.img['data-original']

            price = soup.find_all(attrs={"itemprop": "price"})[i]

            i = i+1
            price = price.text
            price = str(price).replace('৳', '')
            price = str(price).replace(',', '').strip()

            if product.find('div', {'class': 'bottom syn-soldout'}):
                status = "not available"
            else:
                status = "available"

            product_records = {
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title
            }
            total_products.append(product_records)

        url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})

        if url:
            url = url.get('href')
        else:
            break

    print("gaming console done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))


    write_file.close()








