# Title
# Description
# Image

import requests
from bs4 import BeautifulSoup

URL = 'https://www.trademe.co.nz/a/motors/cars/search?bof=mfduxg59&search_string=toyota&user_region=60'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='tm-search-results__container')

job_elems = results.find_all('div', class_='tm-motors-search-card__wrapper ng-star-inserted')

paragraphs = []

for job_elem in job_elems:
	price = job_elem.find('span', class_='tm-motors-search-card__price')
	title = job_elem.find('div', class_='tm-motors-search-card__title h-padding-right-double')
	kms = job_elem.find('span', class_='tm-motors-search-card__body-odometer tm-motors-search-card__body-desc-highlited ng-star-inserted')
	image = job_elem.find('tg-aspect-ratio', class_='o-aspect-ratio o-aspect-ratio--4x3')
	#link = job_elem.find('a', class_='tm-motors-search-card__link')
	print(price.text.strip())
	print(title.text.strip())
	print(kms.text.strip())
	print(image['style'].strip()[21:-2])
	print()
