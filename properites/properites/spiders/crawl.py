import scrapy


class CrawlSpider(scrapy.Spider):
    name = 'crawl'
    allowed_domains = ['web']
    start_urls = ['http://web/']

    def parse(self, response):
        pass
