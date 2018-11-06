# -*- coding: utf-8 -*-
import scrapy


class ThzbtSpider(scrapy.Spider):
    name = 'thzbt'
    allowed_domains = ['thzbt.co"']
    start_urls = ['http://thzbt.co"/']

    def parse(self, response):
        pass
