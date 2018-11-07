# -*- coding: utf-8 -*-
import scrapy
from autohome_image.items import AutohomeImageItem

class AutohomeSpider(scrapy.Spider):
    name = 'autohome'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/3154.html']

    def parse(self, response):
        uibox_list = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uibox_list:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            img_urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            img_urls_https = list(map(lambda url:response.urljoin(url),img_urls))
            item = AutohomeImageItem(category=category, img_urls=img_urls_https)
            yield item
