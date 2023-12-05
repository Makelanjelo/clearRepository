import requests
from bs4 import BeautifulSoup
from time import sleep 

headers  = {"User-Agent":""}

for count in range(1, 7):
	print(count)
	sleep(3)
	url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

	response = requests.get(url, headers=headers)

	soup = BeautifulSoup(response.text, "html.parser") #html.parser

	data = soup.find_all("div", class_="w-full rounded border")

	for i in data:

		name = i.find("h4").text.replace("\n", "")
		price = i.find("h5").text
		url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")

		print(name + "\n" + price + "\n" + url_img + "\n\n")