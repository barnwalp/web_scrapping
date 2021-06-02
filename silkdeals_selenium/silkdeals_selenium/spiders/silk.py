import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector


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
        # img = response.request.meta['screenshot']
        # # int(response.request.meta['driver'].title)

        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)
        # Getting the driver instance in the parse method
        driver = response.request.meta['driver']
        search_input = driver.find_element_by_xpath("//input[@id='search_form_input_homepage']")
        search_input.send_keys('Hello World')
        
        search_input.send_keys(Keys.ENTER)
        # saving screenshot
        # driver.save_screenshot('after_filling.png')

        # convert the current html page to a selector
        html = driver.page_source
        response_obj = Selector(text=html)

        for link in response_obj.xpath("//div[@class='result__extras__url']/a"):
            yield{
                'URL': link.xpath('.//@href').get()
            }

