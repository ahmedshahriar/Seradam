from bs4 import BeautifulSoup
import requests
import json



requests.packages.urllib3.disable_warnings()  # for removing requests warning

session = requests.Session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
}


write_file = open('ucc_products.json', 'w+')
total_products = []
title_list = []
product_url_list = []

def parser(i):
    url = 'http://ucc-bd.com/products-1/all-products.html?p={}'.format(i)
    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, 'html.parser')

    items = soup.findAll("li", {"class": "item"})



    for item in items:
        try:
            title = item.h2.a["title"]
            # print(title)
            href = item.h2.a["href"]
            # print(href)

            title_list.append(title)
            product_url_list.append(href)
            product_records = {
                "product_title": title,
                "product_link": href
            }
            total_products.append(product_records)

        except Exception as e:
            pass


    return title_list, product_url_list, total_products, write_file



if __name__ == "__main__":
    # all_products = []
    for i in range(1, 72):
        title_list, product_url_list, total_products, write_file = parser(i)
        # all_products.append(total_products)
        json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))

