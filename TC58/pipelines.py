# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Tc58Pipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "0", db = "tongcheng")

    def process_item(self, item, spider):
        title = ''.join(item["title"])
        price = ''.join(item["price"])
        houseType = ''.join(item["houseType"])
        link = ''.join(item["link"])
        detail = ''.join(item["detail"])
        method = ''.join(item["method"])
        commity = ''.join(item["commity"])


        sql = "INSERT INTO result(title, price, houseType, link, detail, method, commity) VALUES('"+title+"', '"+price+"', '"+houseType+"', '"+link+"', '"+detail+"', '"+method+"', '"+commity+"')"
        self.conn.query(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()