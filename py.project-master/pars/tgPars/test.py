import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"}

url = f"https://tgstat.ru/tag/bryansk-region"
response = requests.get(url, headers=headers)
html_content = BeautifulSoup(response.text, "html.parser")
block = html_content.find_all("div", class_="col-12 col-sm-6 col-lg-4")

print(html_content)