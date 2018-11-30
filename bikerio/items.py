# -*- coding: utf-8 -*-
import scrapy


class Station(scrapy.Item):
    name = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()

class StationLog(scrapy.Item):
    station = scrapy.Field()
    available_bikes = scrapy.Field()
    empty_docks = scrapy.Field()
    crawl_date = scrapy.Field()