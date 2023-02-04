Take Reference From [Web Scraping with Python, 2nd Edition](https://www.oreilly.com/library/view/web-scraping-with/9781491985564/)



# BeautifulSoup
* html structure
  ```bash
    bs = BeautifulSoup(html, 'html.parser')
    # below produces same results
    bs.h1
    bs.html.body.h1
    bs.body.h1
    bs.html.h1
  ```
  ## children vs decedents vs next sibilings vs parent
  * in general, BS deals with the [descendants](https://pythonscraping.com/pages/page3.html) of the current tag selected
  * if want to find only descendebts that are children, use `.children`

  ## Main Objects
  * BeautifulSoup objects: `bs`
  * Tab Objects: `bs.div.h1`
  * NavigableString Objects
  * Comment Onjects `<!--like this one-->`

  ## parser
  |Type|parser|Advantage|Disadvantage|
  |:---:|:---:|:---|:---|
  |HTML|`html.parser`|||
  |HTML|`lxml`|parse messy or malformed HTML code. Faster than `html.parser`|Depend on C libraries|
  |HTML|`html5lib`|parse messy or malformed HTML code|the slowest one|

## Note
* get_text() - transfor data into plain text - is the last thing to do before scraping the specifc data following the tag structure of a document
* selecting tags should be specifc instead of relative path or the code will be fragile if page layouts change all the time

## find_all vs find
* `find_all(tag, attributes, recursice, text, limit, keywords)`
  * `recursive`: 
    * True: Default. look for tags into the deepest tags
    * False: look for tags into the top-level tags
  * `limit`: 
    * the first x items
  * `keywords`
    * technically redundant
      * can be replaced by regular express or lambda express
      * conflic of varabie name in Python, e.g. class vs class_
    ```python
      title = bs.find_all(id='title', class_='text')
      title = bs.find(id='title')
      title = bs.find('', {'id': 'text'})
    ```
* `find(tag, attributes, recursice, text, keywords)`
  * `limit` = 1
```python
  # find a list of tags
  .find_all(['h1', 'h2', 'h3'])
  # find a tag with specified attributes
  .find_all('span', {'class': {'green', 'red'}})


```

# Handling Exceptions
## Possible Erros
1. the page is not found on the server (there was an error in retrieving it)
 * 404 page not found
 * 500 internal server error
2. the server is not found
3. html tags do not exist
    * bs.None_object.tag: return AttributeError
    * bs.exist_object.none_tag: reutrn None


# Analyze websites
> should not be a hammer to dig all tags and use them. The code is fragile when the structure of tags changes
* look for a "print this page" or "html file" link
* look for the information hidden in a JavaScript file
* look for URL
* use other alternative websites
  * if no, the final way is to select tags by elegant methods: BeautifuleSoup

# Handling Redirects
* server-side redirects
  * URL is changed
  * easy
* client-side redirects
  * JavaScript or HTML

# Web Crawling Models
## Type: crawl different websites
```python
  class Content:
    def __init__(self, url, title, body):
      pass

    def print(slef):
      '''print content'''

  class Crawler:
    def getPage(url):
    
    def safeGet():
      '''make sure all information is crawled, no empty result'''

    def parse():
      '''use getPage and safeGet'''




```

# Scrapy
## Create a project of Scrapy
```bash
  scrapy startproject <project_name>

```