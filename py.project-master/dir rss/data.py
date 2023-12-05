








import pytz
from datetime import datetime
from parser import getContent
for i in getContent():
    titleData = i.title
    content = i.text
    imgData = i.img
    title = "<title>" + titleData + "</title>"
    img = '<enclosure url="' + imgData + '"/>'
    yandexContent = "<yandex:full-text>" + content + "</yandex:full-text>"
    turboContent = "<turbo:content>" + content + "</turbo:content>"
    time = "<pubDate>" + str(datetime.now(tz)) + "</pubDate>"
    print(title, img, yandexContent, turboContent, time)

