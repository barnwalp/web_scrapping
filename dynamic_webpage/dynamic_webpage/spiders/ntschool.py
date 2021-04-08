import scrapy
import json


class NtSchool(scrapy.Spider):
    name = 'ntschool'
    start_urls = [
        'https://directory.ntschools.net/#/schools'
    ]

    def parse(self, response):
        yield scrapy.Request(
            url="https://directory.ntschools.net/api/System/GetAllSchools",
            callback=self.parse_json
        )

    def parse_json(self, response):
        raw_json = response.body
        nl = "\n"
        print(f'Printing raw_json data: {nl}{raw_json}')
        data = json.loads(raw_json)

        for school in data:
            school_code = school["itSchoolCode"]
            yield scrapy.Request(
                f"https://directory.ntschools.net/api/System/GetSchool?itSchoolCode={school_code}",
                callback=self.parse_school,
            )

    def parse_school(self, response):
        data = json.loads(response.body)

        yield {
            "name": data["name"],
            "mail": data["mail"]
        }
