import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector


class ComputerDealsSpider(scrapy.Spider):
    name = 'computer_deals'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://slickdeals.net/computer-deals/',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )
    
    def parse(self, response):
        for link in response.css('.fpItem'):
            yield{
                'product_name': link.css('.itemImageLink a::text').get(),
                'product_price': link.css('.priceLine .itemPrice::text').get()
            }
