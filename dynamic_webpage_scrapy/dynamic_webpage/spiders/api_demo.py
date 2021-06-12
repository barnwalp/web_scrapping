import scrapy
import json
from xml.etree import ElementTree as ET

class ApiSchool(scrapy.Spider):
    name = "apischool"

    def start_requests(self):
        yield scrapy.Request(
            url='https://directory.ntschools.net/api/System/GetAllSchools',
            headers={
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
            })

    def parse(self, response):
        xml_data = response.body
        tree = ET.fromstring(xml_data)

        # getting all tags in elemList
        elemList = []
        for elem in tree.iter():
            elemList.append(elem.tag)
        
        # print(elemList)
        for school in tree.findall('{http://schemas.datacontract.org/2004/07/doe.EducationDirectory.Web.Models}SchoolsForListDto/{http://schemas.datacontract.org/2004/07/doe.EducationDirectory.Web.Models}SchoolName'):
            yield{
                'school_name': school.text,
            }
