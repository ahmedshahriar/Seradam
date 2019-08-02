from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import json
import pprint


def ryans_parse_single_laptop_details(url):

    html = urlopen(url)
    data = html.read()
    soup = BeautifulSoup(data, 'html.parser')
    description = soup.find('div', {'class': 'std'}).text.split("\r\n")
    table = soup.find("tbody")
    trs = table.find_all('tr')

    details = dict(description=description)

    for tr in trs:
        details[tr.find('th').text] = tr.find('td').text

    return details


def ryans_analyze_storage(storage_text):

    storage = dict()

    if "HDD" in storage_text or "hdd" in storage_text or "Hard Disk Drive" in storage_text or "hard drive" in storage_text:
        if 'HDD' in storage_text:
            pos = storage_text.find("HDD")
        elif 'hdd' in storage_text:
            pos = storage_text.find("hdd")
        elif "Hard Disk Drive" in storage_text:
            pos = storage_text.find("Hard Disk Drive")
        else:
            pos = storage_text.find("hard drive")

        storage_amount_type = ""
        for i in range(pos - 1, 1, -1):
            if storage_text[i] == 'B':
                if storage_text[i - 1] == 'T' or storage_text[i - 1] == 'G':
                    pos = i
                    storage_amount_type = storage_text[i - 1] + storage_text[i]
                    break
        pos -= 2
        if storage_text[pos] == ' ':
            pos -= 1

        size = ""
        for i in range(pos, -1, -1):
            if storage_text[i] == ' ' or storage_text[i] == '+':
                break
            size = size + storage_text[i]
        storage["HDD"] = size[::-1] + storage_amount_type

    if "SSD" in storage_text or "ssd" in storage_text:
        if 'SSD' in storage_text:
            pos = storage_text.find("SSD")
        else:
            pos = storage_text.find("ssd")

        storage_amount_type = ""

        for i in range(pos - 1, 1, -1):
            if storage_text[i] == 'B':
                if storage_text[i - 1] == 'T' or storage_text[i - 1] == 'G':
                    pos = i
                    storage_amount_type = storage_text[i - 1] + storage_text[i]
                    break
        pos -= 2
        if storage_text[pos] == ' ':
            pos -= 1

        size = ""
        for i in range(pos, -1, -1):
            if storage_text[i] == ' ' or storage_text[i] == '+':
                break
            size = size + storage_text[i]
        storage["SSD"] = size[::-1] + storage_amount_type

    if "SSH" in storage_text or "ssh" in storage_text:
        if 'SSH' in storage_text:
            pos = storage_text.find("SSH")
        else:
            pos = storage_text.find("ssh")

        storage_amount_type = ""

        for i in range(pos - 1, 1, -1):
            if storage_text[i] == 'B':
                if storage_text[i - 1] == 'T' or storage_text[i - 1] == 'G':
                    pos = i
                    storage_amount_type = storage_text[i - 1] + storage_text[i]
                    break
        pos -= 2
        if storage_text[pos] == ' ':
            pos -= 1

        size = ""
        for i in range(pos, -1, -1):
            if storage_text[i] == ' ' or storage_text[i] == '+':
                break
            size = size + storage_text[i]
        storage["SSH"] = size[::-1] + storage_amount_type

    if len(storage) == 0:

        pos = len(storage_text)
        storage_amount_type = ""

        for i in range(pos - 1, 1, -1):
            if storage_text[i] == 'B':
                if storage_text[i - 1] == 'T' or storage_text[i - 1] == 'G':
                    pos = i
                    storage_amount_type = storage_text[i - 1] + storage_text[i]
                    break
        pos -= 2
        if storage_text[pos] == ' ':
            pos -= 1

        size = ""
        for i in range(pos, -1, -1):
            if storage_text[i] == ' ' or storage_text[i] == '+':
                break
            size = size + storage_text[i]
        storage["HDD"] = size[::-1] + storage_amount_type

    return storage


def ryans_analyze_processor(processor_text):
    processor = ""
    search = "Intel Core i"
    if search in processor_text:
        search_pos = processor_text.find(search)
        key_pos = search_pos + len(search)
        processor = search + processor_text[key_pos]

    return processor


def ryans_parse_laptop_list(url,brand):

    print("Ryans laptop parsing-"+brand)
    json_file = "./json/ryans/laptop/"+brand+".json"


    write_file = open(json_file, 'w')
    total_products = []
    procecor = []
    page = 1
    print("page : ",end="")
    while url:
        print("page {}".format(page))
        page += 1

        # html = urlopen(Request(url, headers=hdr))
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'item-inner'})
        p = 0
        for product in products:
            p += 1

            product_url = product.div.a['href']
            print(product_url)
            img_link = product.div.a.img['src']
            title = product.find('h2', {'class': 'product-name'}).a.text

            price = product.find('p', {'class': 'special-price'})
            if price:
                price = str(price.span.span.text).replace("Tk ", '').replace(',', '')
            else:
                price = str(product.find('div', {'class': 'price-box'}).span.span.text).replace("Tk ", '').replace(',', '')

            try:
                price = int(price)
            except:
                price = price


            details = ryans_parse_single_laptop_details(product_url)

            # doing this because in some product's details this filed may be missing
            if "RAM type" in details.keys():
                ram_type = details['RAM type'].split(' ')[0]
            else:
                ram_type = ""

            if "Display Size" in details.keys():
                display_size = details['Display Size']
            else:
                display_size = ""
            storage = dict()
            if "Storage" in details.keys():
                storage = ryans_analyze_storage(details['Storage'])

            status = "available"

            print(details['Processor'])
            product_records = {
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title,
                "description": details['description'],
                "model": details['Model'],
                "ram": details['RAM'],
                "ram_type": ram_type,
                "brand": brand,
                "graphics_memory": details['Graphics memory'],
                "display_size": display_size,
                "display_type": details['Display Type'],
                "storage": storage,
                "website": "ryanscomputers.com"
            }
            total_products.append(product_records)
            # total_products.append(details['Processor'])
        url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})
        if url:
            url = url.get('href')
        else:
            break

    print(brand+" laptop parsing done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()


def ryans_parse_all_laptop():
    # ryans

    url = "https://ryanscomputers.com/laptop-notebook/acer-laptop-price-all.html"
    brand = 'Acer'
    ryans_parse_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/apple-laptop-all.html"
    brand = 'Apple'
    ryans_parse_laptop_list(url, brand)


    url = "https://ryanscomputers.com/laptop-notebook/asus-laptop-price-all.html"
    brand = 'Asus'
    ryans_parse_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/dell-laptop-price-all.html"
    brand = 'Dell'
    ryans_parse_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/hp-laptop-price-all.html"
    brand = 'HP'
    ryans_parse_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/lenovo-laptop-price-all.html"
    brand = 'Lenovo'
    ryans_parse_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/ilife-laptop-price-all.html"
    brand = 'iLife'
    ryans_parse_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/microsoft.html"
    brand = 'Microsoft'
    ryans_parse_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/msi.html"
    brand = 'MSI'
    ryans_parse_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/fujitsu.html"
    brand = 'Fujitsu'
    ryans_parse_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/chuwi.html"
    brand = 'Chuwi'
    ryans_parse_laptop_list(url, brand)

