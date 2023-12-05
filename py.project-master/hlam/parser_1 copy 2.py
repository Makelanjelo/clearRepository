import requests
from bs4 import BeautifulSoup
from time import sleep 

headers  = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
def download(url):
	resp = requests.get(url, stream = True)
	r = open("C:\\Users\\Markel\\Desktop\\image\\" + url.split("/")[-1], "wb")
	for value in resp.iter_content(1024*1024):
		r.write(value)
	r.close()

def get_url():
	for count in range(1, 7):
		url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
		response = requests.get(url, headers=headers)
		soup = BeautifulSoup(response.text, "html.parser") #html.parser
		data = soup.find_all("a", class_="w-full rounded border")
		for i in data:
			card_url = "https://scrapingclub.com" + i.find("a").get("href")
			yield card_url
def array():
	for card_url in get_url():

			response = requests.get(card_url, headers=headers)
			sleep(1)
			soup = BeautifulSoup(response.text, "html.parser") #html.parser

			data = soup.find("div", class_="my-8 w-full rounded border")
			name = data.find("h3").text
			price = data.find("h4").text
			text = data.find("p").text
			url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top").get("src")
			download(url_img)
			yield name, price, text, url_img