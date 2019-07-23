from bs4 import BeautifulSoup
from urllib.request import urlopen
import json


def startech_laptop_list_org(url,brand):


    print("Startech laptop parsing-"+brand)
    json_file = "./json/startech/laptop/"+brand+".json"

    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    print("page : ", end="")

    while url:
        print(" {},".format(page),end="")
        page += 1
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'product-thumb'})
        p=1
        for product in products:
            p+=1
            product_url = product.find('div',{'class': 'img-holder'}).a['href']
            img_link = product.find('div',{'class': 'img-holder'}).a.img['src']
            title = product.find('h4', {'class': 'product-name'}).a.text
            price = product.find('div', {'class': 'price space-between'}).span.text.replace('৳','').replace(',','')
            status = product.find('i',{'class' : 'fa fa-shopping-cart'})
            if status:
                status="available"
            else:
                status="not available"
            product_records = {
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title,
                # 'id': id,
                "brand": brand
            }
            # id +=1
            total_products.append(product_records)
        # url = soup.find('ul', {'class': 'pagination'}).ul.find_all('li')[-1].a
        url = soup.find('ul', {'class': 'pagination clearfix'})
        # print("url: ")

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



def get_laptop_description(url):
    print(url)
    html = urlopen(url)
    data = html.read()
    soup = BeautifulSoup(data, 'html.parser')
    description = soup.find("div", {"class": "short-description"})

    print(description)

    return description


def startech_laptop_list(url,brand):


    print("Startech laptop parsing-"+brand)
    json_file = "./json/startech/laptop/"+brand+".json"

    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    print("page : ", end="")

    while url:
        print(" {},".format(page),end="")
        page += 1
        html = urlopen(url)
        data = html.read()
        soup = BeautifulSoup(data, 'html.parser')
        products = soup.find_all('div', {'class': 'product-thumb'})
        p=1
        for product in products:
            p+=1
            product_url = product.find('div',{'class': 'img-holder'}).a['href']
            img_link = product.find('div',{'class': 'img-holder'}).a.img['src']
            title = product.find('h4', {'class': 'product-name'}).a.text
            price = product.find('div', {'class': 'price space-between'}).span.text.replace('৳','').replace(',','')
            status = product.find('i',{'class' : 'fa fa-shopping-cart'})
            if status:
                status="available"
            else:
                status="not available"
            product_records = {
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title,
                # 'id': id,
                "brand": brand
            }
            # id +=1
            total_products.append(product_records)
        # url = soup.find('ul', {'class': 'pagination'}).ul.find_all('li')[-1].a
        url = soup.find('ul', {'class': 'pagination clearfix'})
        # print("url: ")

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




def startech_all_laptop():
    url = "https://www.startech.com.bd/laptop-notebook/laptop/razer-laptop"
    brand = 'razer'
    startech_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/apple-macbook"
    brand = 'apple'
    startech_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/asus-laptop"
    brand = 'asus'
    startech_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/acer-laptop"
    brand = 'acer'
    startech_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/dell-laptop"
    brand = 'dell'
    startech_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/hp-laptop"
    brand = 'hp'
    startech_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/lenovo-laptop"
    brand = 'lenovo'
    startech_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/microsoft-surface-pro"
    brand = 'microsoft'
    startech_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/i-life-laptop"
    brand = 'ilife'
    startech_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/msi-laptop"
    brand = 'msi'
    startech_laptop_list(url, brand)

    url = "https://www.startech.com.bd/laptop-notebook/laptop/chuwi"
    brand = 'chuwi'
    startech_laptop_list(url, brand)
