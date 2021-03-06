# -*- coding: utf-8 -*-
import scrapy
from TC58.items import Tc58Item


class Tc58Spider(scrapy.Spider):
    name = 'tc58'
    allowed_domains = ['nj.58.com']
    start_urls = ['http://nj.58.com/jiangning/hezu/0/?PGTID=0d30000a-00b9-517a-920c-54a3803d2cf3&ClickID=4']

    detailLink = 'www.nj.58.com'
    pageNum = 1

    def parse(self, response):
        lis = response.xpath('/html/body/div[3]/div[1]/div[5]/div[2]/ul/li')
        count = 0
        for li in lis:
            if len(li.xpath('div[2]/h2/a/@href').extract()) != 0 and count < 100:
                link = li.xpath('div[2]/h2/a/@href').extract()[0]
                count = count + 1
                self.detailLink = link
                yield scrapy.Request(url=link, callback = self.parseDetail)

# set the pages to crawl
        if self.pageNum < 10:
            self.pageNum += 1
            if len(response.xpath('//*[@id="bottom_ad_li"]/div[2]/a[12]/@href').extract()) != 0:
                nextPageLink = (response.xpath('//*[@id="bottom_ad_li"]/div[2]/a[12]/@href').extract()[0])
                yield scrapy.Request(url = nextPageLink, callback = self.parse)

    def parseDetail(self, response):
        item = Tc58Item()
        item['title'] = response.xpath('/html/body/div[4]/div[1]/h1/text()').extract()
        item['price'] = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/div/span[1]/b/text()').extract()
        item['houseType'] = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/span[2]/text()').extract()
        item['detail'] = response.xpath('/html/body/div[4]/div[3]/div[1]/div[1]/ul/li/span[2]/text()').extract()
        item['method'] = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[1]/span[2]/text()').extract()
        item['link'] = self.detailLink
        item['commity'] = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[4]/span[2]/a/text()').extract()
        return item