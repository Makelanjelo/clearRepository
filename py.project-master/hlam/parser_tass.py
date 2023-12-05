import requests
from bs4 import BeautifulSoup
from time import sleep 
headers  = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
def get_url():
	url = f"https://moskva.bezformata.com/"

	response = requests.get(url, headers=headers)

	html_content = BeautifulSoup(response.text, "html.parser")
	section = html_content.find("section", class_="hottopicbox")
	cards = section.find_all("article")
	for i in cards:
		card_url = i.find("a").get("href")
		yield card_url
	#print(list_url)
def array():
	for card_url in get_url():

		response = requests.get(card_url, headers=headers)

		html_content = BeautifulSoup(response.text, "html.parser")
		
		name = html_content.find("h1").text
		author = html_content.find("div", class_="sourcetopicbox")
		author_link = author.find("a").get("href")
		yield card_url, name, author.text, author_link

# for x in array():
# 	print(type(x))