# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging


class SilkdealsSeleniumPipeline:
    # Purpose of this method is to grab whatever value you want
    # from settings.py file
    @classmethod
    def from_crawler(cls, crawler):
        # print the value of MONGO_URI defined in settings.py
        logging.warning(crawler.settings.get('MONGO_URI'))

    # It will be called when spider starts execution process
    def open_spider(self, spider):
        logging.warning("SPIDER OPENED FROM PIPELINE")
    
    # It will be called when spider finishes execution
    def close_spider(self, spider):
        logging.warning("SPIDER CLOSED FROM PIPELINE")

    # For each item scrapped, process_item method is called
    def process_item(self, item, spider):
        return item
