# -*- coding: utf-8 -*-
import scrapy
from xiaosuo.items import XiaosuoItem
from .sort import Cn2An,get_tit_num

class XiaosSpider(scrapy.Spider):
    name = 'xiaos'
    allowed_domains = ['qu.la']
    start_urls = ['http://www.qu.la/paihangbang/']
    novel_list=[]
    def parse(self, response):
        books=response.xpath('.//div[@class="index_toplist mright mbottom"]')
        for book in books:
            link=book.xpath('.//div[2]/div[2]/ul/li[1]')
            for li in link:
                url='http://www.qu.la'+li.xpath('.//a/@href').extract()[0]
                self.novel_list.append(url)
        self.novel_list=list(set(self.novel_list))
        for nov in self.novel_list:
            yield scrapy.Request(nov,callback=self.get_page_url)

    def get_page_url(self,response):

        pages=response.xpath('.//dd/a/@href').extract()
        for url in pages:
            yield scrapy.Request('http://www.qu.la'+url,callback=self.get_text)

    def get_text(self,response):
        item=XiaosuoItem()
        item['bookname'] = response.xpath('.//div[@class="con_top"]/a[2]/text()').extract()[0]

        # 章节名 ,将title单独找出来，为了提取章节中的数字
        title = response.xpath('.//h1/text()').extract()[0]
        item['title'] = title

        #  找到用于排序的id值
        item['order_id'] = Cn2An(get_tit_num(title))

        # 正文部分需要特殊处理
        body = response.xpath('.//div[@id="content"]/text()').extract()

        # 将抓到的body转换成字符串，接着去掉\t之类的排版符号，
        text = ''.join(body).strip().replace('\u3000', '')
        item['body'] = text
        return item




