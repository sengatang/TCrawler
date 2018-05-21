#coding:utf-8
import scrapy
from scrapy.selector import Selector
from qqnews.items import QqnewsItem
from scrapy_redis.spiders import RedisCrawlSpider
import re
class newsSpider(RedisCrawlSpider):
    print('here')
    redis_key = 'newsSpider:start_urls'  #redis 设置
    print(redis_key)
    # start_urls = ['http://news.qq.com','http://ent.qq.com/','http://finance.qq.com/']
    name='tencent'
    url = ''
    def parse(self, response):
        # date = response.xpath('//*[@id="echoData"]/text()').extract()
        # print("今天的日期是%s" % date)
        container = response.xpath('//a/@href').extract()
        print(len(container))
        for url in container:
            if 'http' in url or 'qq' in url: #or 'qq' in url 
                # print(url)
                yield scrapy.Request(url, self.parseNews)

    
    def parseNews(self,response):
        item = QqnewsItem()
        title = response.xpath("//h1/text()").extract()
        item['title'] = title
        content = response.xpath("//p/text()").extract()
        cc = ''
        if(len(content)>0):
            for c in content:
                cc = cc+c+'\n'
        item['text'] = cc
        return item





