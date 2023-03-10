import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'

    def start_requests(self):
        urls = [
            'https://zh.wikipedia.org/zh-tw/Python',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python'
        ]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response): # callback function
        url = response.url
        title = response.css('title:text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))
    