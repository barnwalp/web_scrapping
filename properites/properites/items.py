# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Items, Field


class ProperitesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # primary fields
    title = Field()
    price = Field()
    description = Field()
    address = Field()
    image_urls = Field()

    # calculated fields
    images = Field()
    location = Field()

    # housekeeping fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
    pass
