from bs4 import BeautifulSoup
from urllib.request import urlopen
import json




def product_list_scrap(url):
	total_products = []
	# write_file = open('bagdoom_mobile_tabs_products.json', 'w+')
	# write_file = open('bagdoom_camera_products.json', 'w+')
	write_file = open('bagdoom_home_appliances_products.json', 'w+')
	while url:
		html = urlopen(url)
		data = html.read()
		soup = BeautifulSoup(data, "html.parser")
		
		total_products_in_page = []
		
		title_list = []
		product_url_list = []
		count = 0
		tags = soup.find_all('h2', class_='product-name')
		print(len(tags))
		for tag in tags:
			title = tag.a['title']
			product_url = tag.a['href']
			
			title_list.append(title)
			product_url_list.append(product_url)
			
			product_records = {
				"product_title": title,
				"product_link": product_url
			}
			
			total_products_in_page.append(product_records)
		print(total_products_in_page)
		
		total_products.extend(total_products_in_page)
		print(total_products)
		
		url = soup.find('a', {'class': 'next i-next', 'title': 'Next'})
		print(url)
		if url:
			url = url.get('href')
		else:
			break
		
		
	json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
	write_file.close()
	return


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


bagdoom_computer_url = "https://www.bagdoom.com/electronics/computers-laptops.html?limit=78&p=1"
bagdoom_mobile_tabs_url = "https://www.bagdoom.com/electronics/mobiles-tabs.html?limit=78&p=1"
bagdoom_product_url = "https://www.bagdoom.com/catalog/product/view/id/249969/s/beats-tm-030-bluetooth-headphone-blue-copy-02/category/765/"

bagdoom_camera_url = "https://www.bagdoom.com/electronics/camera.html?limit=78&p=1"
bagdoom_home_appliances_url = "https://www.bagdoom.com/electronics/home-appliances.html?limit=78&p=1"

print(product_list_scrap(bagdoom_home_appliances_url))
# print(product_details_scrap(startech_product_url))
