import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from worldmeters.worldmeters.spiders.countries import CountriesSpider


# This will import spider settings
process = CrawlerProcess(settings=get_project_settings())
process.crawl(CountriesSpider)
process.start()