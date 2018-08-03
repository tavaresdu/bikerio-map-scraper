# -*- coding: utf-8 -*-
import scrapy
from bikerio import items
from scrapy.selector import Selector


class BikerioMapSpider(scrapy.Spider):
    name = 'bikerio_map'
    allowed_domains = ['bikeitau.com.br']
    start_urls = ['https://bikeitau.com.br/bikerio/mapa-das-estacoes/']

    def parse(self, response):
        for element in response.selector.xpath('//ul[@id="infoWind"]/li'):
            element = Selector(text=element.extract())
            for station in element.xpath('//div[contains(@class, "infoAdd")]/text()'):
                station = station.extract().split('-')
                item = items.Station()
                item['id'] = station[0].strip()
                item['name'] = station[1].strip()
                yield item
        # station = items.Station()
        # station_log = items.StationLog()
        # for e in response.xpath(xbase + 'div[contains(@class, "infotxt")]/text()').extract():
        #     print(e)
