import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

url = input("URL: ")
response = requests.get(url, headers=headers)
html_content = BeautifulSoup(response.text, "html.parser")
block = html_content.find_all("div", class_="col-12 col-sm-6 col-lg-4")

def get_data():
    for i in block:
        name = i.find("div", class_="font-16 text-dark text-truncate").text
        link = i.find("a", class_="text-body").get("href")
        description = i.find("div", class_="font-14 text-muted line-clamp-2 mt-1").text
        content = i.find("div", class_="font-12 text-body").text
        realm = i.find("div", class_="font-12 text-truncate").text
        link_response = requests.get(link, headers=headers)
        link_html_content = BeautifulSoup(link_response.text, "html.parser")
        tgLink = link_html_content.find("a",
                                        class_="btn btn-outline-info btn-rounded px-3 py-05 font-14 mr-1 mb-15").get("href")
        yield name, tgLink, description.strip(), content.strip(), realm.strip()

print(get_data())