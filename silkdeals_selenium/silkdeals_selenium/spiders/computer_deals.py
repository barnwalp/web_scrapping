import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
import re


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
                'product_link': link.css('.itemImageLink a::attr(href)').get(),
                'product_price': self.normalize_whitespace(link.css('.priceLine .itemPrice::text').get()),
                'store_name': link.css('.itemStore.bp-p-storeLink::text').get()
            }

    def normalize_whitespace(self, str):
        # removing whitespace from front and tail of string
        str = str.strip()
        # removing unicode chanracter from the strings
        str = str.encode("ascii", "ignore").decode()
        # re.sub replace occurence of particular substring with another
        # substring. In this case occurence of 1 or more whitespce in between
        # words are replaced with one whitespace
        str = re.sub(r'\s+', ' ', str)
        return str
