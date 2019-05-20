
'''
Andre Dasalla
Version 1.0.0
May 20, 2019
'''

import requests
from bs4 import BeautifulSoup 

def search(title): 
	site = "https://www.123movies.gdn/?s=" + title
	r = requests.get(site)
	data = r.content
	soup = BeautifulSoup(data, "html.parser")
	links = soup.find_all("a", { "class": "ml-mask jt"})
	for link in links:
		print(link.text)
		print(link['href'])
	

def main():
	print("Movie Site Searcher")
	print("Created By: Andre Dasalla")
	print("Version 1.0")

	title = input("\nEnter Title of Movie: ")
	title = title.replace(" ", "+")
	print('\nSearching for links containing "{}"'.format(title))
	search(title)
	

main()
