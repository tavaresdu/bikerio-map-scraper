# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from datetime import datetime
from bikerio import items
import scrapy
import re


class BikerioMapSpider(scrapy.Spider):
    name = 'bikerio_map'
    allowed_domains = ['bikeitau.com.br']
    start_urls = ['https://bikeitau.com.br/bikerio/mapa-das-estacoes/']

    def parse(self, response):
        name_xpath = '//div[@class="infoAdd"]/text()'
        log_xpath = '//div[@class="infotxt"]/text()'
        for s in response.selector.xpath('//ul[@id="infoWind"]/li'):
            s = Selector(text=re.sub(r'[\n\t]', '', s.extract(), 
                flags=re.MULTILINE))
            station = items.Station()
            station['name'] = s.xpath(name_xpath).extract()[0]
            yield station
            log = items.StationLog()
            log['station'] = station['name']
            log_extracted = s.xpath(log_xpath).extract()
            log['available_bikes'] = int(log_extracted[0].replace(': ', ''))
            log['empty_docks'] = int(log_extracted[1].replace(': ', ''))
            log['crawl_date'] = datetime.now()
            yield log