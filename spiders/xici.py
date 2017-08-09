# -*- coding: utf-8 -*-
import scrapy
from Proxy.items import XiciItem

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://xicidaili.com']

    def start_requests(self):
        reqs = []
        
        for i in range(1,31):
            req = scrapy.Request('http://www.xicidaili.com/nn/%s'%i)
            print('req ========',req)
            reqs.append(req)
        return reqs
    
    def parse(self, response):
        ip_list = response.xpath('/html/body/div[1]/div[2]/table')
        trs = ip_list[0].xpath('tr')
        
        item = []
        
        for ip in trs[1:]:
            pre_item = XiciItem()
            pre_item['IP'] = ip.xpath('td[2]/text()')[0].extract()
            pre_item['PORT'] = ip.xpath('td[3]/text()')[0].extract()    
            pre_item['POSITION'] = ip.xpath('td[4]/a/text()')[0].extract()
            pre_item['TYPE'] = ip.xpath('td[6]/text()')[0].extract()
            pre_item['LAST_CHECK_TIME'] = ip.xpath('td[10]/text()')[0].extract()
            print('pre_item',pre_item)
            item.append(pre_item)
        return item