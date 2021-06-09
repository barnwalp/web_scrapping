# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import logging
import pymongo
import os


class MongodbPipeline(object):
    collection_name = 'best_deals'
    # Purpose of this method is to grab whatever value you want
    # from settings.py file
    # @classmethod
    # def from_crawler(cls, crawler):
    #     # print the value of MONGO_URI defined in settings.py
    #     logging.warning(crawler.settings.get('MONGO_URI'))

    # It will be called when spider starts execution process
    def open_spider(self, spider):
        # logging.warning("SPIDER OPENED FROM PIPELINE")
        # MongoClient takes host and port it connects to
        password = os.getenv('MONGO_PASS')
        self.client = pymongo.MongoClient('mongodb+srv://pankaj:Toptal@21@cluster0.cso4b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        # Deals is the databse name here
        self.db = self.client["Deals"]
    
    # It will be called when spider finishes execution
    # def close_spider(self, spider):
    #     # logging.warning("SPIDER CLOSED FROM PIPELINE")
    #     # Close the client connection like garbage collection
    #     self.client.close()

    # For each item scrapped, process_item method is called
    def process_item(self, item, spider):
        # insert each item in the database
        self.db[self.collection_name].insert(item)
        return item
