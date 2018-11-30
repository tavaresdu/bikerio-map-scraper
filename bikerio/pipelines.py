# -*- coding: utf-8 -*-
from bikerio.spiders.bikerio_map import BikerioMapSpider
from bikerio import items
import sqlite3


class BikerioPipeline(object):
    path = 'bikerio/db/'
    db_name = 'bikerio.db'
    conn = None

    def open_spider(self, spider):
        if self.conn is None:
            self.conn = sqlite3.connect(self.path + self.db_name)
        self.start_db()

    def process_item(self, item, spider):
        cursor = self.conn.cursor()
        if type(item) is items.Station:
            self.save_station(item, cursor)
        elif type(item) is items.StationLog:
            self.save_station_log(item, cursor)
        cursor.close()
        return item

    def start_db(self):
        cursor = self.conn.cursor()
        with open(self.path + 'create_station.sql', 'r') as sql:
            cursor.execute(sql.read())
        with open(self.path + 'create_station_log.sql', 'r') as sql:
            cursor.execute(sql.read())
        cursor.close()
    
    def save_station(self, item, cursor):
        station_id = self.get_station_id(item['name'], cursor)
        if station_id >= 0:
            return
        with open(self.path + 'insert_station.sql', 'r') as sql:
            cursor.execute(sql.read(), (item['name'],))
            self.conn.commit()
    
    def save_station_log(self, item, cursor):
        item['station'] = self.get_station_id(item['station'], cursor)
        if item['station'] < 0:
            raise Exception(item)
        with open(self.path + 'insert_station_log.sql', 'r') as sql:
            cursor.execute(sql.read(), (item['station'],
                item['available_bikes'], item['empty_docks'],
                item['crawl_date']))
            self.conn.commit()

    def get_station_id(self, name, cursor):
        with open(self.path + 'select_station_id_by_name.sql', 'r') as sql:
            cursor.execute(sql.read(), (name,))
            station_id = cursor.fetchone()
            if station_id is not None:
                return station_id[0]
            else:
                return -1

    def close_spider(self, spider):
        self.conn.close()