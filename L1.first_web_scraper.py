from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('https://www.twse.com.tw/holidaySchedule/holidaySchedule?response=html&queryYear=112')
#bs = BeautifulSoup(html.read(), 'html.parser')
#bs = BeautifulSoup(html, 'html.parser')
bs = BeautifulSoup(html.read(), 'lxml')

print(bs.h2)