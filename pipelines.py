# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyPipeline(object):
    def process_item(self, item, spider):
        return item

import pymysql

def dbHandle():
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = '111111',
        charset = 'utf8',
        db = 'Proxy',
        use_unicode = False
    )
    return conn

class XiciPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        sql = 'insert into Proxy.xici(ip,port,type,position,last_check_time) values(%s,%s,%s,%s,%s)'
        lis = (item['IP'],item['PORT'],item['TYPE'],item['POSITION'],item['LAST_CHECK_TIME'])
        
        try:
            cursor.execute(sql,lis)
            dbObject.commit()
            print(item['IP'],'writen sucessed')
        
        except Exception as e:
            print('DB writer failllllll',e)
            dbObject.rollback()
        else:
            #print('DB writer success')
            dbObject.close()

        return item