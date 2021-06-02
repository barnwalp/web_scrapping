import scrapy
from scrapy_selenium import SeleniumRequest


class SilkSpider(scrapy.Spider):
    name = 'silk'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):
        img = response.request.meta['screenshot']
        # print(response.request.meta['driver'].title)

        with open('screenshot.png', 'wb') as f:
            f.write(img)
