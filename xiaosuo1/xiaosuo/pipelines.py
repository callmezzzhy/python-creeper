# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class XiaosuoPipeline(object):
    def process_item(self, item, spider):
        name = item['bookname']
        order_id = item['order_id']
        body = item['body']
        title = item['title']

        # 与本地数据库建立联系
        # 和本地的scrapyDB数据库建立连接
        with open ('{}\t{}.txt'.format(name,title),'a')as f:
            f.write(title+'\n')
            f.write(body)
            print('当前小说：{} 当前章节{} 已经下载完毕'.format(name, title))