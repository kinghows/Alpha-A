# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    date = scrapy.Field()
    time = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    detail = scrapy.Field()
    theme = scrapy.Field()
    stock_group = scrapy.Field()