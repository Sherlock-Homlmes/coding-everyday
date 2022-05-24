import requests
from bs4 import BeautifulSoup
import bs4

import io, json

#from bettermenews_database.crawl import *

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

#print(scrap_by_page_number(2))
#for title in scrap_by_page_number(2):
	#print(title)
