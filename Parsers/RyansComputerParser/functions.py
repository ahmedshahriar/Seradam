from bs4 import BeautifulSoup
from urllib.request import urlopen
import json


def get_laptop_list():


    print("Ryans laptop parsing")
    json_file = "./json/computer_list.json"
    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    print("page : ",end="")
    url = "https://ryanscomputers.com/laptop-notebook.html"
    while url:
        print("{} ".format(page),end="")
        page += 1
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'item-inner'})

        for product in products:
            product_url = product.div.a['href']
            img_link = product.div.a.img['src']
            title = product.find('h2', {'class': 'product-name'}).a.text

            price = product.find('p', {'class': 'special-price'})
            if price:
                price = str(price.span.span.text).replace("Tk ", '').replace(',', '')
            else:
                price = str(product.find('div', {'class': 'price-box'}).span.span.text).replace("Tk ", '').replace(',',
                                                                                                                   '')
            status = ""
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

    print("laptop parsing done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()








def get_tablet_list():


    print("Ryans tablet parsing")
    json_file = "./json/tablet_list.json"
    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    url = "https://ryanscomputers.com/tablet-pc/all-brands.html"
    print("page: ",end="")
    while url:
        print("{} ".format(page),end="")
        page += 1
        html = urlopen(url)
        data = html.read()

        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'item-inner'})
        for product in products:
            product_url = product.div.a['href']
            img_link = product.div.a.img['src']
            title = product.find('h2', {'class': 'product-name'}).a.text

            price = product.find('p', {'class': 'special-price'})
            if price:
                price = str(price.span.span.text).replace("Tk ", '').replace(',', '')
            else:
                price = str(product.find('div', {'class': 'price-box'}).span.span.text).replace("Tk ", '').replace(',',
                                                                                                                   '')

            status = ""
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

    print("tablet parsing done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()








def get_components_list():

    print("Ryans component parsing")
    json_file = "./json/components_list.json"
    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    print("page: ", end="")

    url = "https://ryanscomputers.com/components.html"
    while url:
        print("{} ".format(page),end="")
        page += 1
        html = urlopen(url)
        data = html.read()

        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'item-inner'})
        for product in products:
            product_url = product.div.a['href']
            img_link = product.div.a.img['src']
            title = product.find('h2', {'class': 'product-name'}).a.text

            price = product.find('p', {'class': 'special-price'})
            if price:
                price = str(price.span.span.text).replace("Tk ",'').replace(',','')
            else:
                price = str(product.find('div', {'class': 'price-box'}).span.span.text).replace("Tk ",'').replace(',','')

            status = ""
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

    print("component parsing done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()








def get_monitor_list():

    print("Ryans monitor parsing")
    json_file = "./json/monitor_list.json"
    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    print("page: ", end="")

    url = "https://ryanscomputers.com/monitor.html"
    while url:
        print("{} ".format(page),end="")
        page += 1
        html = urlopen(url)
        data = html.read()

        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'item-inner'})

        for product in products:
            product_url = product.div.a['href']
            img_link = product.div.a.img['src']
            title = product.find('h2', {'class': 'product-name'}).a.text

            price = product.find('p', {'class': 'special-price'})
            if price:
                price = str(price.span.span.text).replace("Tk ",'').replace(',','')
            else:
                price = str(product.find('div', {'class': 'price-box'}).span.span.text).replace("Tk ", '').replace(',', '')

            status = ""
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

    print("monitor parsing done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()







def get_storage_list():

    print("Ryans storage parsing")
    json_file = "./json/storage_list.json"
    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    print("page: ", end="")

    url = "https://ryanscomputers.com/storage.html"
    while url:
        print("{} ".format(page),end="")
        page += 1
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'item-inner'})

        for product in products:
            product_url = product.div.a['href']
            img_link = product.div.a.img['src']
            title = product.find('h2', {'class': 'product-name'}).a.text

            price = product.find('p', {'class': 'special-price'})
            if price:
                price = str(price.span.span.text).replace("Tk ",'').replace(',','')
            else:
                price = str(product.find('div', {'class': 'price-box'}).span.span.text).replace("Tk ", '').replace(',', '')

            status = ""
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

    print("storage parsing done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()






def get_Photography_list():

    print("Ryans photography parsing")
    json_file = "./json/photography_list.json"
    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    print("page: ", end="")

    url = "https://ryanscomputers.com/photography.html"
    while url:
        print("{} ".format(page),end="")
        page += 1
        html = urlopen(url)

        data = html.read()

        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'item-inner'})

        for product in products:
            product_url = product.div.a['href']
            img_link = product.div.a.img['src']
            title = product.find('h2', {'class': 'product-name'}).a.text

            price = product.find('p', {'class': 'special-price'})
            if price:
                price = str(price.span.span.text).replace("Tk ",'').replace(',','')
            else:
                price = str(product.find('div', {'class': 'price-box'}).span.span.text).replace("Tk ", '').replace(',', '')

            status = ""
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

    print("photography parsing done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()







def get_network_list():

    print("Ryans network parsing")
    json_file = "./json/network_list.json"
    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    print("page: ", end="")

    url = "https://ryanscomputers.com/network.html"
    while url:
        print("{} ".format(page),end="")
        page += 1
        html = urlopen(url)
        data = html.read()

        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'item-inner'})

        for product in products:
            product_url = product.div.a['href']
            img_link = product.div.a.img['src']
            title = product.find('h2', {'class': 'product-name'}).a.text

            price = product.find('p', {'class': 'special-price'})
            if price:
                price = str(price.span.span.text).replace("Tk ",'').replace(',','')
            else:
                price = str(product.find('div', {'class': 'price-box'}).span.span.text).replace("Tk ", '').replace(',', '')

            status = ""
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

    print("network parsing done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()







def get_AudioVideo_list():

    print("Ryans audiovideo parsing")
    json_file = "./json/AudioVideo_list.json"
    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    print("page: ", end="")

    url = "https://ryanscomputers.com/audio-video.html"
    while url:
        print("{} ".format(page),end="")
        page += 1
        html = urlopen(url)
        data = html.read()

        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'item-inner'})

        for product in products:
            product_url = product.div.a['href']
            img_link = product.div.a.img['src']
            title = product.find('h2', {'class': 'product-name'}).a.text

            price = product.find('p', {'class': 'special-price'})
            if price:
                price = str(price.span.span.text).replace("Tk ",'').replace(',','')
            else:
                price = str(product.find('div', {'class': 'price-box'}).span.span.text).replace("Tk ", '').replace(',', '')

            status = ""
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

    print("audiovideo parsing done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()









def get_accessories_list():

    print("Ryans accessories parsing")
    json_file = "./json/accessories_list.json"
    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    print("page: ", end="")

    url = "https://ryanscomputers.com/accessories.html"
    while url:
        print("{} ".format(page),end="")
        page += 1
        html = urlopen(url)
        data = html.read()

        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'item-inner'})
        print("total products: {}".format(len(products)))
        for product in products:
            product_url = product.div.a['href']
            img_link = product.div.a.img['src']
            title = product.find('h2', {'class': 'product-name'}).a.text

            price = product.find('p', {'class': 'special-price'})
            if price:
                price = str(price.span.span.text).replace("Tk ",'').replace(',','')
            else:
                price = str(product.find('div', {'class': 'price-box'}).span.span.text).replace("Tk ", '').replace(',', '')

            status = ""
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

    print("accessories parsing done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()

















