# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItnewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    kind = scrapy.Field()
    title = scrapy.Field()
    display = scrapy.Field()
    author = scrapy.Field()

class StockItem(scrapy.Item):
    name = scrapy.Field()
    open_price = scrapy.Field()
    previous_price = scrapy.Field()
    price = scrapy.Field()
