from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

####### csv dump
# def product_list_scrap(url):
# 	html = urlopen(url)
# 	data = html.read()
# 	soup = BeautifulSoup(data, "html.parser")
#
# 	title_list = []
# 	product_url_list = []
# 	tags = soup.find_all('h4', class_='product-name')
# 	writeFile =  open('startech_products.csv', 'w',newline='')
# 	writer = csv.writer(writeFile)
# 	writer.writerow(["Product Title", "Product Link"])
# 	for tag in tags:
# 		title = tag.a.text
# 		product_url = tag.a['href']
# 		title_list.append(title)
# 		product_url_list.append(product_url)
# 		writer.writerow([str(title),product_url])
#
# 	writeFile.close()
# 	return title_list,product_url_list

def product_list_scrap(url):
	html = urlopen(url)
	data = html.read()
	soup = BeautifulSoup(data, "html.parser")
	write_file = open('startech_products.json','w+')
	total_products = []
	title_list = []
	product_url_list = []
	tags = soup.find_all('h4', class_='product-name')

	for tag in tags:
		title = tag.a.text
		product_url = tag.a['href']
		title_list.append(title)
		product_url_list.append(product_url)
		product_records = {
			"product_title":title,
			"product_link" :product_url
		}
		total_products.append(product_records)
	
	json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
	return title_list,product_url_list
	


def product_details_scrap(url):
	html = urlopen(url)
	data = html.read()
	soup = BeautifulSoup(data, "html.parser")
	category_info_list = []
	
	
	
	category_tag_breakpoint = soup.find('ul', class_='breadcrumb')
	category_tags = category_tag_breakpoint.findAll('li')
	
	for tag in category_tags[:-1]:
		category_info_list.append(tag.text)
	
	category_info_list.pop(0)
	
	return category_info_list
	

startech_url = "https://www.startech.com.bd/product/search?&search=+&limit=4598"
startech_product_url = "https://www.startech.com.bd/adp-cat-6-cable"

print(product_list_scrap(startech_url))
# print(product_details_scrap(startech_product_url))
