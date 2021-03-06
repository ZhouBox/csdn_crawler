# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from csdn.items import CsdnItem, CsdnArticleItem
#/zhx6044/article/details/45698535

class CsdnCrawlerSpider(CrawlSpider):
    name = 'csdn_crawler'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['http://blog.csdn.net/zhx6044']

    rules = (
        Rule(LinkExtractor(allow=r'article/list/[0-9]{1,20}'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'article/details/[0-9]{1,20}'), callback='parse_article', follow=True),
    )

    def parse_item(self, response):
        i = CsdnItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['title'] = response.xpath('//*[@id="article_list"]/div[@class="list_item article_item"]/div[@class="article_title"]/h1/span/a/text()').extract()
        i['url'] = response.xpath('//*[@id="article_list"]/div[@class="list_item article_item"]/div[@class="article_title"]/h1/span/a/@href').extract()
        return i

    def parse_article(self, response):
        i = CsdnArticleItem()
        i['title'] = response.xpath('//*[@id="article_details"]/div[1]/h1/span/a/text()').extract()
        i['article'] = response.xpath('//*[@id="article_content"]').extract()
        return i
