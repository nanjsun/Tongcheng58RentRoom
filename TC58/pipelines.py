# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Tc58Pipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "0", db = "ScrapyTongcheng")

    def process_item(self, item, spider):
        title = item["title"][0]
        link = item["link"][0]
        sql = "INSERT INTO result(title, link) VALUES('dafdadf', '"+link+"')"
        # sql = "INSERT INTO result(link) VALUES('"+link+"')"
        self.conn.query(sql)
        return item

    def close_spider(self, spider):
        self.conn.close()
