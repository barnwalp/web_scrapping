import scrapy
from scrapy_splash import SplashRequest


class BeerSpider(scrapy.Spider):
    name = 'beer'

    def start_requests(self):
        url = 'https://www.beerwulf.com/en-gb/c/mixedbeercases'
        yield SplashRequest(url)

    def parse(self, response):
        products = response.css(".product.search-product.draught-product.notranslate.pack-product")
        for item in products:
            yield{
                'name': item.css("h4::text").get(),
                'price': item.css("span.price::text").get()
            }
