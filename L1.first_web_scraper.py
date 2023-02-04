from urllib.request import urlopen
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup

html = urlopen('https://www.twse.com.tw/holidaySchedule/holidaySchedule?response=html&queryYear=112')
#bs = BeautifulSoup(html.read(), 'html.parser')
#bs = BeautifulSoup(html, 'html.parser')
bs = BeautifulSoup(html.read(), 'lxml')
print(bs.h2)

try: 
    html = urlopen('https://www.twse.com.tw/holidaySchedule/holidaySchedule?response=html&queryYear=112')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found')
else: # if no exception, continue else
    print('It Worked!')


try:
    badContent = bs.nonExistingTag.anotherTag
except AttributeError as e:
    print('Tag was not found')
else:
    if badContent == None:
        print('Tag was not found')
    else:
        print(badContent)
