# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Tc58Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    houseType = scrapy.Field()
    link = scrapy.Field()
    detail = scrapy.Field()
    method = scrapy.Field()
    commity = scrapy.Field()

    pass
