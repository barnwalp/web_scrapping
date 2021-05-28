import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


# This spider is inhereting from crawlspider class
class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    # allowed_domains = ['x']
    start_urls = ['http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']
    # rules is tuple; wherein Rule is an object which tells the crawlspider
    # what are the links you want to follow. In this case you must pass
    # callback method which must not be parse
    # LinkExtractor extract all links which contains 'Items' in the url
    # Instead of allow, you can also pass deny argument which will ensure
    # that specified urls are not extracted
    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(deny=r'Items/'), callback='parse_item', follow=True),
        # you can also use xpath or css to extract link. please note that href
        # argument is not passed as object is capable in extracting links
        # Rule(LinkExtractor(restrict_xpaths=('//a[@class="active"]')), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_css=('.lister-item-header a')), callback='parse_item', follow=True),
    )

    def parse_test(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    def parse_item(self, response):
        yield{
            'title': self.normalize_whitespace(response.css("h1::text").get()),
            'year': response.css("#titleYear a::text").get(),
            'duration': self.normalize_whitespace(response.css("time::text").get()),
            'genre': response.css(".subtext a::text").get(),
            'rating': response.css(".ratingValue span::text").get(),
            'movie_url': response.url
        }
        print(response.url)

    def normalize_whitespace(self, str):
        str = str.strip()
        str = re.sub(r'\s+', ' ', str)
        return str
