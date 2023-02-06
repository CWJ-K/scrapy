from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ArticleSpider(CrawlSpider):
    '''
    The spider traverses wikipedia.org, following all links under the domain wikipedia.org,
    printing titles of pages, and ignoring all external (offsite) links.
    '''
    name = 'article'

    # Tells spider to start crawling from and whether it should follow or ignore a link based on the domain
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']

    # All article pages starting with /wiki/ and not containing a colon are passed to the parse_items
    rules = [
        # cb_kwargs: pass keyword arguments to callback functions
        Rule(
            LinkExtractor(allow='^(/wiki/)((?!:).)*$'),
            callback='parse_items',
            follow=True,
            cb_kwargs={'is_article': True}
        ),
        # allow all the URLs
        Rule(
            LinkExtractor(allow=r'.*'),
            callback='parse_items',
            cb_kwargs={'is_article': False}
        )
    ]

    def parse_items(self, response, is_article):
        print(response.url)
        title = response.css('title::text').extract_first()

        if is_article:
            text = response.xpath(
                '//div[@id="mw-content-text"]//text()').extract()
            lastUpdated = response.css(
                'li#footer-info-lastmod::text').extract_first()
            lastUpdated = lastUpdated.replace(
                'This page was last edited on', ''
            )
            print('Title is: {}'.format(title))
            print('Text is: {}'.format(text))
            print('Last updated: {}'.format(lastUpdated))
        else:
            print('This is not an article: {}'.format(title))
