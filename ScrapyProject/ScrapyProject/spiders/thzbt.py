# -*- coding: utf-8 -*-
import scrapy


class ThzbtSpider(scrapy.Spider):
    name = 'thzbt'
    allowed_domains = ['thzbt.co"']
    start_urls = ['http://thzbt.co/forum-181-1.html']

    def parse(self, response):
        print(response)
