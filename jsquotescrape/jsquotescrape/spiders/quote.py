import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['w']
    start_urls = ['http://w/']

    def parse(self, response):
        pass
