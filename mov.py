
'''
Andre Dasalla
Version 1.0.1
May 20, 2019
'''

import requests
from bs4 import BeautifulSoup 

def search(newTitle, title): 
	site = "https://www.123movies.gdn/?s=" + newTitle
	r = requests.get(site)
	data = r.content
	soup = BeautifulSoup(data, "html.parser")
	links = soup.find_all("a", { "class": "ml-mask jt"})
	for link in links:
		if (link.text.lower() == title.lower()):
			print(link.text)
			print(link['href'])
			break
		else:
			print(link.text)
			print(link['href'])
	

def main():
	print("Movie Site Searcher")
	print("Created By: Andre Dasalla")
	print("Version 1.0")

	title = input("\nEnter Title of Movie: ")
	newTitle = title.replace(" ", "+")
	print('\nSearching for links containing "{}"'.format(title))
	search(newTitle, title)
	

main()
