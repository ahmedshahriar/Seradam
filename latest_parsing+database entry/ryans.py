from bs4 import BeautifulSoup
from urllib.request import urlopen
import json



def get_laptop_description(url):
    html = urlopen(url)
    data = html.read()
    soup = BeautifulSoup(data, 'html.parser')
    description = soup.find_all('div', {'class': 'std'})[0].text
    model = soup.find_all('td',{'class':'data'})[1].text
    return description, model

def get_laptop_list(url,brand):


    print("Ryans laptop parsing-"+brand)
    json_file = "./json/ryans/laptop/"+brand+".json"

    write_file = open(json_file, 'w')
    total_products = []
    page = 1
    print("page : ",end="")

    while url:
        print(" {},".format(page),end="")
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
                price = str(product.find('div', {'class': 'price-box'}).span.span.text).replace("Tk ", '').replace(',', '')

            description,model = get_laptop_description(product_url)
            description= description.replace("\r\n","<br/>")
            status = ""
            product_records = {
                "status": status,
                "img_link": img_link,
                "price": price,
                "product_link": product_url,
                "product_title": title,
                "description": description,
                "model": model,
                "brand": brand
            }
            total_products.append(product_records)
        url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})
        if url:
            url = url.get('href')
        else:
            break

    print(brand+" laptop parsing done")

    json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
    write_file.close()








def ryans_all_laptop():
    # ryans

    url = "https://ryanscomputers.com/laptop-notebook/acer-laptop-price-all.html"
    brand = 'acer'
    get_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/apple-laptop-all.html"
    brand = 'apple'
    get_laptop_list(url, brand)


    url = "https://ryanscomputers.com/laptop-notebook/asus-laptop-price-all.html"
    brand = 'asus'
    get_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/dell-laptop-price-all.html"
    brand = 'dell'
    get_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/hp-laptop-price-all.html"
    brand = 'hp'
    get_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/lenovo-laptop-price-all.html"
    brand = 'lenovo'
    get_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/ilife-laptop-price-all.html"
    brand = 'ilife'
    get_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/microsoft.html"
    brand = 'microsoft'
    get_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/msi.html"
    brand = 'msi'
    get_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/fujitsu.html"
    brand = 'fujitsu'
    get_laptop_list(url, brand)

    url = "https://ryanscomputers.com/laptop-notebook/chuwi.html"
    brand = 'chuwi'
    get_laptop_list(url, brand)



