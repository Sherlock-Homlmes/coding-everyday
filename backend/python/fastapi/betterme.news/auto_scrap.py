import requests
from bs4 import BeautifulSoup
import bs4

import io, json

#from bettermenews_database.crawl import *

topic = ["khoa-hoc","lich-su","dia-ly","sinh-hoc",
         "10-van-cau-hoi-vi-sao","su-that-thu-vi","1001-bi-an","danh-nhan-the-gioi","the-gioi-dong-vat",
         "y-hoc-suc-khoe","kien-truc-doc-dao"]


##### scrap
def scrap_by_page_number(number):
	response = requests.get(f"https://khoahoc.tv/?p={number}")
	soup = BeautifulSoup(response.content, "html.parser")

	post_view = soup.findAll('div', class_='listview')
	post_list = []
	post_dict = {}
	for view in post_view:
		temporary = view.findAll('li', class_='listitem clearfix')
		for tempo in temporary:
			###include: title, thumb, desc

			#title
			title = tempo.find('a','title')
			title_content = title.contents[0]
			href = title.get("href")

			#thumb
			thumb = tempo.find('a',class_='thumb')
			thumb = thumb.find('img')
			thumb_alt = thumb.get('alt')
			thumb_src = thumb.get('data-src')

			
			#desc
			desc = tempo.find('div',class_='desc')
			desc = desc.contents[0]

			#h
			#post_list.append(tempo)
			post_dict[f"{href}"] = {
			"title_content": title_content,
			"thumb_src": thumb_src,
			#"thumb_alt": thumb_alt,
			"description": desc
			}


	#slider_view = soup.findAll('div', class_='slider')

	with io.open('check_data.json', 'w', encoding='utf-8') as f:
   		json.dump(post_dict, f, ensure_ascii=False, indent=4)

	return post_dict
	#soup.prettify()

def title_process(title:str) -> str:
	title = title[1::]
	tit = title.split("-")
	tit.pop()

	title = '-'.join(tit)
	return title


##### process after scrap
def auto_scrap_process(check_list:list,html_type_list:list,tags_list:list):
	for check in check_list:
		html = []
		tag  = []
		for html_type in html_type_list:
			if html_type.startswith(check):
				html_type = html_type.split("|||")[1]
				if html_type not in topic:
					return False
				else:
					html.append(html_type)
		for tags in tags_list:
			if tags.startswith(check):
				tags = tags.split("|||")[1]
				if tags not in ["normal","horror"]:
					return False
				else:
					tag.append(tags)	

		print(f"html: {html}")
		print(f"tag: {tag}")