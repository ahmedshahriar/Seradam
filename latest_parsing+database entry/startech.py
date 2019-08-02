from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import pprint
import time


def startech_parse_single_laptop_details(url):
    html = urlopen(url)
    data = html.read()
    soup = BeautifulSoup(data, 'html.parser')
    details = dict()
    tbody = soup.find("tbody")
    try:
        trs = tbody.find_all("tr")
    except:
        return details

    for tr in trs:
        tds = tr.find_all("td")
        details[tds[0].text] = tds[1].text

    return details


def startech_analyze_display_size(display_text):

    display_size = ""
    special = "\""
    special2 = "”"
    special3 = "'"
    if special in display_text:
        pos = display_text.find(special)
        size = ""
        for i in range(pos, -1, -1):
            if display_text[i] == ' ':
                break
            size = size + display_text[i]
        display_size = size[::-1]

    elif special2 in display_text:
        size = ""
        pos = display_text.find(special2)
        pos -= 1
        for i in range(pos, -1, -1):
            if display_text[i] == ' ':
                break
            size = size + display_text[i]
        display_size = size[::-1] + "\""

    elif special3 in display_text:
        size = ""
        pos = display_text.find(special3)
        pos -= 1
        for i in range(pos, -1, -1):
            if display_text[i] == ' ':
                break
            size = size + display_text[i]
        display_size = size[::-1] + "\""

    elif "inch" in display_text:
        pos = display_text.find("inch")
        pos -= 1
        if display_text[pos] == '-':
            pos -= 1
        size = ""
        for i in range(pos, -1, -1):
            if display_text[i] == ' ':
                break
            size = size + display_text[i]
        display_size = size[::-1] + "\""

    return display_size


def startech_analyze_storage(storage_text):

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
            if storage_text[i] >= '0' and storage_text[i] <= '9':
                size = size + storage_text[i]
            else:
                break

        storage["HDD"] = size[::-1] + storage_amount_type

    if "SSD" in storage_text or "ssd" in storage_text:
        if 'SSD' in storage_text:
            pos = storage_text.find("SSD")
        else:
            pos = storage_text.find("ssd")
        storage_amount_type = ""

        found = False
        for i in range(pos - 1, 1, -1):
            if storage_text[i] == 'B':
                if storage_text[i - 1] == 'T' or storage_text[i - 1] == 'G':
                    pos = i
                    storage_amount_type = storage_text[i - 1] + storage_text[i]
                    found = True
                    break
        if found:
            pos -= 2
            if storage_text[pos] == ' ':
                pos -= 1
            size = ""
            for i in range(pos, -1, -1):
                if storage_text[i] >= '0' and storage_text[i] <= '9':
                    size = size + storage_text[i]
                else:
                    break
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
        found = False
        for i in range(pos - 1, 1, -1):
            if storage_text[i] == 'B':
                if storage_text[i - 1] == 'T' or storage_text[i - 1] == 'G':
                    pos = i
                    storage_amount_type = storage_text[i - 1] + storage_text[i]
                    found = True
                    break
        pos -= 2

        if found:
            if storage_text[pos] == ' ':
                pos -= 1
            size = ""
            for i in range(pos, -1, -1):
                if storage_text[i] >= '0' and storage_text[i] <= '9':
                    size = size + storage_text[i]
                else:
                    break

            storage["HDD"] = size[::-1] + storage_amount_type

    return storage


def startech_analyze_processor(processor_text):
    processor = "Others"

    search1 = "Intel Core i"
    search2 = "AMD Ryzen"
    search3 = "Intel Core M"

    if "Intel" in processor_text:

        if search1 in processor_text:
            search_pos = processor_text.find(search1)
            key_pos = search_pos + len(search1)
            processor = search1 + processor_text[key_pos]
        elif "Intel Cor i" in processor_text:
            search_pos = processor_text.find("Intel Cor i")
            key_pos = search_pos + len("Intel Cor i")
            processor = "Intel Core i" + processor_text[key_pos]
        elif "Intel Corei" in processor_text:
            search_pos = processor_text.find("Intel Corei")
            key_pos = search_pos + len("Intel Corei")
            processor = "Intel Core i" + processor_text[key_pos]
        elif "i3" in processor_text:
            processor = "Intel Core i3"
        elif "i5" in processor_text:
            processor = "Intel Core i5"
        elif "i7" in processor_text:
            processor = "Intel Core i7"


    if search2 in processor_text:
        search_pos = processor_text.find(search2)
        key_pos = search_pos + len(search2) + 1
        processor = search2 + " " + processor_text[key_pos]

    if search3 in processor_text:
        search_pos = processor_text.find(search3)
        key_pos = search_pos + len(search3)
        processor = search3 + processor_text[key_pos]

    if "AMD" in processor_text:
        if "E2" in processor_text:
            processor = "AMD E2"
        if "A4" in processor_text:
            processor = "AMD A4"
        if "A9" in processor_text:
            processor = "AMD A9"
        if "A6" in processor_text:
            processor = "AMD A6"
        if "E1" in processor_text:
            processor = "AMD E1"


    return processor


def startech_parse_laptop_list(url,brand):

    print("Startech laptop parsing-"+brand)

    json_file = "./json/startech/laptop/"+brand+".json"
    write_file = open(json_file, 'w')

    total_products = []
    page = 1
    print("page : ", end="")
    count = 1
    while url:
        print(" {},".format(page),end="")
        page += 1
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'product-thumb'})

        for product in products:
            count += 1
            product_url = product.find('div',{'class': 'img-holder'}).a['href']
            img_link = product.find('div',{'class': 'img-holder'}).a.img['src']
            title = product.find('h4', {'class': 'product-name'}).a.text
            price = product.find('div', {'class': 'price space-between'}).span.text.replace('৳','').replace(',','')

            try:
                price = int(price)
            except:
                price = price


            product_url = product_url.replace(' ','%20')
            print(product_url)
            img_link = img_link.replace(' ','%20')

            """
                description parsing is not working well, data fetching partially. 
                description = product.find('duv', {'class': 'descriptions'})
                doing it manually
            """
            description = []

            status = product.find('i',{'class' : 'fa fa-shopping-cart'})

            if status is not None:
                status = "available"
            else:
                status = "not available"

            details = startech_parse_single_laptop_details(product_url)

            if len(details) == 0:
                continue

            processor = ""
            if "Processor" in details.keys():

                details["Processor"] = details["Processor"].replace("®",'')
                details["Processor"] = details["Processor"].replace("™",'')
                processor = startech_analyze_processor(details["Processor"])

                description.append("Processor - " + processor)
            else:
                print("no processor")

            display_size = ""
            if "Display" in details.keys():
                display_size = startech_analyze_display_size(details["Display"])
                description.append("Display Size - " + display_size)

            ram = ""
            ram_type = ""
            if "Memory" in details.keys():

                ram_text = details['Memory']
                pos = ram_text.find("GB")
                pos -= 1
                if ram_text[pos] == ' ':
                    pos -= 1
                size = ""

                for i in range(pos, -1, -1):
                    if ram_text[i]>='0' and ram_text[i]<='9':
                        size = size + ram_text[i]
                    else:
                        break

                if len(size) > 0:
                    ram = size[::-1] + "GB"
                    description.append("RAM - " + ram)

                if 'DDR4' in ram_text:
                    ram_type = "DDR4"
                    description.append("RAM Type- " + ram_type)

                if 'DDR3' in ram_text:
                    ram_type = "DDR3"
                    description.append("RAM Type- " + ram_type)

            storage = dict()
            if "Storage" in details.keys():
                storage = startech_analyze_storage(details["Storage"])
                data = ""
                if "HDD" in storage.keys():
                    data += "HDD - " + storage["HDD"] + " "
                if "SSD" in storage.keys():
                    data += "SSD - " + storage["SSD"] + " "
                if "SSH" in storage.keys():
                    data += "SSH - " + storage["SSH"] + " "
                description.append(data)

            graphics_memory = ""

            if "Graphics" in details.keys():
                graphics_text = details["Graphics"]

                graphics_memory = "Shared"

                if "GB" in graphics_text:
                    pos = graphics_text.find("GB")
                    pos -= 1
                    if graphics_text[pos] == ' ':
                        pos -= 1
                    size = ""

                    for i in range(pos, -1, -1):
                        if graphics_text[i] >= '0' and graphics_text[i] <= '9':
                            size = size+graphics_text[i]
                        else:
                            break

                    graphics_memory = size[::-1]+"GB"
                description.append("Graphics Memory - "+graphics_memory)


            product_records ={
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title,
                "description": description,
                "ram": ram,
                "ram_type": ram_type,
                "brand": brand,
                "graphics_memory": graphics_memory,
                "display_size": display_size,
                "storage": storage,
                "processor": processor,
                "website": "startech.com.bd"
            }

            total_products.append(product_records)

        url = soup.find('ul', {'class': 'pagination clearfix'})
        if url:
            url = url.ul
            if url:
                url = url.find_all('li')
                if url:
                    url = url[-1]
                    if url:
                        url = url.a
                        if url:
                            url = url['href']
                        else:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            break

    print(brand+" laptop parsing done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()


def startech_parse_all_laptop():

    url = "https://www.startech.com.bd/laptop-notebook/laptop/razer-laptop"
    brand = 'Razer'
    startech_parse_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/apple-macbook"
    brand = 'Apple'
    startech_parse_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/asus-laptop"
    brand = 'Asus'
    startech_parse_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/acer-laptop"
    brand = 'Acer'
    startech_parse_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/dell-laptop"
    brand = 'Dell'
    startech_parse_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/hp-laptop"
    brand = 'HP'
    startech_parse_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/lenovo-laptop"
    brand = 'Lenovo'
    startech_parse_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/microsoft-surface-pro"
    brand = 'Microsoft'
    startech_parse_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/i-life-laptop"
    brand = 'iLife'
    startech_parse_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/msi-laptop"
    brand = 'MSI'
    startech_parse_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/chuwi"
    brand = 'Chuwi'
    startech_parse_laptop_list(url, brand)

