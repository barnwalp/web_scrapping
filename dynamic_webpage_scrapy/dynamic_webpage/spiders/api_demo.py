import scrapy
from scrapy.utils.response import open_in_browser
import xmltodict


class ApiSchool(scrapy.Spider):
    name = "apischool"

    def start_requests(self):
        yield scrapy.Request(
            url='https://directory.ntschools.net/api/System/GetAllSchools',
            headers={
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
            })

    def parse(self, response):
        # open_in_browser(response)
        print(type(response))
        print(xmltodict.parse(response))
