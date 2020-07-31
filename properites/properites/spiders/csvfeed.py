import scrapy


class CsvfeedSpider(scrapy.Spider):
    name = 'csvfeed'
    allowed_domains = ['web']
    start_urls = ['http://web/']

    def parse(self, response):
        pass
