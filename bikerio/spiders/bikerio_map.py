# -*- coding: utf-8 -*-
import scrapy
from bikerio import items
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import re


class BikerioMapSpider(scrapy.Spider):
    name = 'bikerio_map'
    allowed_domains = ['bikeitau.com.br']
    start_urls = ['https://bikeitau.com.br/bikerio/mapa-das-estacoes/']

    def parse(self, response):
        for element in response.selector.xpath('//ul[@id="infoWind"]/li'):
            element = Selector(text=element.extract())
            value_type = None
            for station_log in element.xpath('//div/descendant-or-self::*/text()'):
                line = station_log.extract().strip()
                if re.match(r'\d+ - [\w\s]+', line):
                    item = items.Station()
                    station = line.split('-')
                    item['id'] = station[0].strip()
                    item['name'] = station[1].strip()
                    yield item
                elif 'Vagas Livres' in line:
                    value_type = 'V'
                elif 'Bicicletas Disponíveis' in line:
                    value_type = 'B'
                elif ':' in line:
                    value_type = None