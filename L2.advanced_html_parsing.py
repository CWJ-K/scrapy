from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.find_all('span', {'class': 'green'})
for name in nameList:
    pass
    #print(name.get_text())

# Navigating Trees
html = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')
#for child in bs.find('table', {'id': 'giftList'}).children:
#for child in bs.find('table', {'id': 'giftList'}).descendants:
for child in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    pass
    #print(child)

print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())