import scrapy
import json

class NtSchool(scrapy.Spider):
    name = 'ntschool'
    start_urls = [
        'https://directory.ntschools.net/#/schools'
    ]

    def parse(self, response):
        yield scrapy.Request(
            url = "https://directory.ntschools.net/api/System/GetAllSchools",
            callback = self.parse_json
        )
    
    def parse_json(self, response):
        pass