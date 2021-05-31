import scrapy


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass
