# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Station(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()

class StationLog(scrapy.Item):
    station_id = scrapy.Field()
    available_bikes = scrapy.Field()
    empty_docks = scrapy.Field()
    crawl_date = scrapy.Field()
    last_update = scrapy.Field()
    weekday = scrapy.Field()
