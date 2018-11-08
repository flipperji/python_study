# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 内置下载器
"""
    Files Pipeline  Image Pipeline
    使用步骤
        1.在items里面定义两个属性 file_urls(存储下载文件url的链接) files || image_urls images
        2.当文件下载完成后，会把文件下载的相关信息存储到item的files(images)属性中，比如下载路径、下载的url等
        3.在配置文件settings.py中
            3.1设置FILES_STORE(IMAGES_STORE)，这个用来配置文件下载下来的路径
            3.2在ITEM_PIPELINES中设置scrapy.pipelines.files.FilesPipeline:1(scrapy.pipelines.images.ImagesPipeline:1)
"""
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from autohome_image import settings
class AutohomeImagePipeline(object):
    def __init__(self):
        # 获取项目下面images文件夹绝对路径
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        # 如果文件件路径不存在则创建
        if not os.path.exists(self.path):
            os.mkdir(self.path)


    def process_item(self, item, spider):
        category = item['category']
        img_urls = item['img_urls']
        category_path = os.path.join(self.path, category)
        # 创建类目文件夹
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for img_url in img_urls:
            img_name = img_url.split('_')[-1]
            # 调用request方法下载图片
            request.urlretrieve(img_url, os.path.join(category_path, img_name))
        return item
# 自定义的pipeline 设置文件存储路径， 如果不走自定义的方式，文件会被默认存储在full文件夹内
class AutohomeImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs = super(AutohomeImagesPipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        path = super(AutohomeImagesPipeline, self).file_path(request, response, info)
        category =request.item.get('category')
        image_store = settings.IMAGES_STORE
        category_path = os.path.join(image_store, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace("full/", "")
        image_path = os.path.join(category_path, image_name)
        return image_path
