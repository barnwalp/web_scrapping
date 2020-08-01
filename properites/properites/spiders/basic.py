import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://web:9312/properties/property_000000.html']

    def parse(self, response):
        self.log('title: %s' %response.xpath(
            '//*[@itemprop="name"][1]/text()').extract())
        self.log('price: %s' %response.xpath(
            '//*[@itemprop="price"][1]/text()').re('[.0-9]+'))

