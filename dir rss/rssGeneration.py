import datetime
from parserV2 import getContent

currentDate = datetime.date.today().isoformat()
myFile = open("parss.xml", "w")
container = ('<rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/" '
             'xmlns:yandex="http://news.yandex.ru" xmlns:turbo="http://turbo.yandex.ru" '
             'version="2.0"><channel><title>'
             '</title><description>'
             '</description><link></link><lastBuildDate>'
             '</lastBuildDate><generator>Smarty3</generator><image><url>'
             '</url><title>'
             '</title><link></link></image><item turbo="true">')
myFile.write(container)


def writer(parametr):
    for item in parametr():
        titleRss = '<item turbo="true">' "<title>" + item[0] + "</title>"
        imgRSS = '<enclosure url="' + f"https://www.gorodtorzhok.ru" + item[1] + '"/>'
        yandex = "<yandex:full-text>" + item[2] + "</yandex:full-text>"
        content = "</turbo:content>" + item[2] + "</turbo:content>"
        timeRss = "<pubDate>" + currentDate + "</pubDate>" + "</item>"
        myFile.write(titleRss + imgRSS + yandex + content + timeRss)


writer(getContent)
myFile.write("</channel></rss>")
