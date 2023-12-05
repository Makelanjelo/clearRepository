from bs4 import BeautifulSoup
import requests
import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                  "Safari/537.36"}
url = f"https://www.gorodtorzhok.ru/news/"
response = requests.get(url, headers=headers)
htmlContent = BeautifulSoup(response.text, "lxml")
block = htmlContent.find_all("div", class_="main_news__newsblock")
myFile = open("parss.xml", "w")
currentDate = datetime.date.today().isoformat()
container = ('<rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/" '
             'xmlns:yandex="http://news.yandex.ru" xmlns:turbo="http://turbo.yandex.ru" '
             'version="2.0"><channel><title>'
             '</title><description>'
             '</description><link></link><lastBuildDate>'
             '</lastBuildDate><generator>Smarty3</generator><image><url>'
             '</url><title>'
             '</title><link></link></image><item turbo="true">')
myFile.write(container)
for i in block[0: 4]:
    subUrl = f"https://www.gorodtorzhok.ru" + i.find("a").get("href")
    response1 = requests.get(subUrl, headers=headers)
    blockContent = BeautifulSoup(response1.text, "lxml")
    content = blockContent.find("section", class_="main__topnews")
    title = "<title>" + content.find("h1").text + "</title>"
    img = '<enclosure url="' + f"https://www.gorodtorzhok.ru" + content.find("img").get("src") + '"/>'
    yandexContent = "<yandex:full-text>" + content.find("div", class_="articletext").text + "</yandex:full-text>"
    turboContent = "<turbo:content>" + content.find("div", class_="articletext").text + "</turbo:content>"
    time = "<pubDate>" + currentDate + "</pubDate>"

    myFile.write(title + img + yandexContent + turboContent + time + "</item>\n")
myFile.write("</channel></rss>")
