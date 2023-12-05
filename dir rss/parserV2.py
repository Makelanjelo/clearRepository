from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                  "Safari/537.36"}


def getUrl():
    url = f"https://www.gorodtorzhok.ru/news/"
    response = requests.get(url, headers=headers)
    htmlContent = BeautifulSoup(response.text, "lxml")
    block = htmlContent.find_all("div", class_="main_news__newsblock")
    for i in block[0: 4]:
        subUrl = f"https://www.gorodtorzhok.ru" + i.find("a").get("href")
        yield subUrl


def getContent():
    for subUrl in getUrl():
        response1 = requests.get(subUrl, headers=headers)
        blockContent = BeautifulSoup(response1.text, "lxml")
        content = blockContent.find("section", class_="main__topnews")
        title = content.find("h1").text
        img = content.find("img").get("src")
        text = content.find("div", class_="articletext").text
        yield title, img, text