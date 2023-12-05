import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}

url = f"https://tgstat.ru/tag/crimea"
response = requests.get(url, headers=headers)
html_content = BeautifulSoup(response.text, "html.parser")
block = html_content.find("div", class_="content p-0 col")
name = block.find_all("div", class_="font-16 text-dark text-truncate")
disclaymer = block.find_all("div", class_="font-14 text-muted line-clamp-2 mt-1")
tema = block.find_all("div", class_="font-12 text-body")
people = block.find_all("b")
print(name)