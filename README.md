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

## Run a spider
```bash
  scrapy runspider <file_name>

  # produce output:
  scrapy runspider <file_name> -o <file_name>.csv -t csv
  scrapy runspider <file_name> -o <file_name>.json -t json
  scrapy runspider <file_name> -o <file_name>.xml -t xml

```

## Selector
* XPath
  * retrieve text content including text in child tags
    * e.g. `<a> tag` inside a block of text
* CSS 
  * all text within child tags will be ignored

## Rule
  |Arguments|Meaning|
  |:---:|:---|
  |link_extractor|e.g. LinkExtractor object|
  |callback|function to parse the content on the page|
  |cb_kwargs|a dictionary of arguments to passed to the callback function|
  |follow|whether links found at the page to be included in a future crawl. default: True, if no callback function is provided. Fasle, if callback function is provided|

### LinkExtractor
* to recognize and return links in a page of HTML content based on the rules provided to it
* accept or deny a link based on CSS and XPath selectors, tag, domains and more
* Main arguments:
  |Arguments|Meaning|
  |allow|allow all links that match the provided regular expression|
  |deny|deny all links that match the provided regular expression|


# Item Pipeline
* improve the speed of your web scraper by perfoming all data processing with waiting for requests to be returned, rather than 
waiting for data to be processed before making another request
  => asychronously

* `settings.py`
  ```python
    # integer presents the order as multiple classes run in the pipeline
    # the range of number typically used: 0-1000, run in ascending order
    ITEM_PIPELINES = {
      "wikiSpider.pipelines.WikispiderPipeline": 300,
    }
  
  ```

* In Spider, `parse_item`: must return Item object. The only goal is to extract the raw data, doing as little processing as possible
  * tasks should be independent
* In pipeline, `process_item`: mandatory method. Scrapy uses it to asynchronously pass Items that are collected by the spider

## Note => Uncertain
* Item-specific parsing may be better handled in the spider, before the data hits the pipeline
* if the parsing takes a long time, you may want to consider moving it to the pipeline (where it can be processed asynchronously) and add a check on the item type 
  ```python
    def process_item(self, item, spider):
      if isinstance(item, Article):
        # Article-specific processing here
  ```

## Logging
* `settings.py`: `LOG_LEVEL = 'ERROR'`

* control logs from command line => unknow issue
```python
scrapy crawl <spider_name> -s LOG_FILE=<log_name>.log

```

# Scrape JavaScript
* JavaScript manipulate the HTML and CSS to display websites
## Common JavaScript Libraries
### jQuery
* identifiable: code contains an import to jQuery
  ```javescript
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></scrip>
  ```
* Ajax and Dynamic HTML: dynamically creates HTML content that appears only after the JavaScript is executed
  * traditional scraping method: retrieve only the preloaded page that appears before the JavaScript has created the content
  * Ajax: Asynchronous JavaScript and XML
    * send information to and receive it from a web server without making a separate page request
      * e.g. fill forms, buttons
    * Ajax is not a language but a group of technologies used to accomplish a certain task by front-end
  
### Google Analytics
* cookies to track your vists from page to page
* can be a problem for web scrapers that are designed to execute JavaScript and handle cookies, e.g. Selenium

### DHTML
* dynamic HTML 

## Solutions
1. scrape the content directly from the JavaScripts
   1. APIs (??)
2. use Python packages execute the JavaScript
   1. Selenium


# Crawl through APIs
* API
  * define a standardized syntax that allows one piece of software to communicate with another piece of software, even if wriiten in different languages or other structured
  * allow a Java Program to communicate with a Python program running on the same machine
  * response from the API is usually returned in a JSON or XML format
    * JSON is far more popular in modern times than XML
      * JSON is lighter than XML
      * JSON is easier to handle by modern server-side technologies, e.g. Angular or Backbone
* ip-api.com easy-to-use and simple API that translates IP addressed to actual physical addresses
  ```website
    http://ip-api.com/xml/36.226.41.31
    http://ip-api.com/csv/36.226.41.31
  ```
## Request information from a web server by HTTP
* POST, PUT, DELETE requests allow users to send information in the body of request
### GET
* make no changes to the information in the server's database. Information is only read
  > hey, web server, please retrieve/get me this information

### POST
* when users fill out a form or submit information, presumably to a backend script on the server, e.g. create a new user
  > Please, store this information in your database
### PUT
* update an object or information, e.g. update the users' email address

### DELETE
* delete an object

## Python Library
### JSON
* JSON parsing library
* Python turns JSON objects into dictionaries, JSON arrays into lists, JSON strings into strings, and so forth
  
```python
  import json
  # transfer json objects into python objects
  json_object = '{"id": 985, "Name": "aswe", "Email": "sdfer@example.com"}'
  python_object = json.loads(str1)

  #transfer python objects into json objects
  python_object = {'id': 985, 'Name': 'aswe', 'Email': 'sdfer@example.com'}
  json_object = json.dumps(j)

```

# Avoid Scraping Traps
1. change Heading
* especially `User-Agent`, not using `Python-urllib/3.4` (default setting of Requests library)
* mobile devices have lacking advertisements and distractions. Can use the heading of mobile devices to scrape webs

2. handling cookies with JavaScript
* EditThisCookie, a Chrome extension
  
3. Time
* multithreaded programming  may be a terrible policy for writing good scrapers

# Human Checklist
1. If the page to be scraped is blank, missing information but information can be seen in the browser
   > Ajax and Dynamic HTML

2. Check the actual POST request sent on Chrome's Inspector panel to make sure all parameters are not missed

3. If logging into a site and can not make the login "stick", or the website is experiencing other strange "state" behaviour.
   > Check cookies being persisted correctly between each page load 

4. get HTTP errors, e.g. 403 Forbidden errors. It may indicate that website has identified your IP address as a bot and is unwilling to accept any more requests
   > 1. wait until your IP address is removed from the list
   > 2. obtain a new IP address
  * Avoid scraps being blocked
     1. change headers
        > copy your own browser's headers
     2. Make sure not clicking on or accessing anything that a human normally would not be able to
     3. contact web adminstratod. They may share their data

