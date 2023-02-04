from urllib.request import urlopen
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print('The server could not be found')
    
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.hi.h1
        if title == None:
            print('Tag was not found')
            return None
    except AttributeError as e:
        print('Object was not found')
        return None
    return title
    

url = getTitle('https://www.twse.com.tw/holidaySchedule/holidaySchedule?response=html&queryYear=112')

print(url)