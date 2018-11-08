# -*- coding: utf-8 -*-
import scrapy
from ..items import AutohomeImageItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class AutohomeSpider(CrawlSpider):
    name = 'autohome'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/3154.html']

    rules = (
        Rule(LinkExtractor(allow=r"https://car.autohome.com.cn/pic/series/3154.+"), callback='parse_page', follow=True),
    )
    # def parse(self, response):
    #     uibox_list = response.xpath("//div[@class='uibox']")[1:]
    #     for uibox in uibox_list:
    #         category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
    #         img_urls = uibox.xpath(".//ul/li/a/img/@src").getall()
    #         img_urls_https = list(map(lambda url: response.urljoin(url), img_urls))
    #         item = AutohomeImageItem(category=category, image_urls=img_urls_https)
    #         yield item
    def parse_page(self, response):
        category = response.xpath("//div[@class='uibox']/div/text()").get()
        #images = response.xpath("//div[@class='uibox']//li/a/img/@src").getall()
        images = response.xpath("//div[contains(@class,'uibox-con')]/ul/li//img/@src").getall()
        image_urls = list(map(lambda url: response.urljoin(url.replace('t_', '')), images))
        yield AutohomeImageItem(category=category,image_urls=image_urls)