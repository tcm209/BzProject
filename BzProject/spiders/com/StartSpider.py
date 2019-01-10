#-*- coding: utf-8 -*-
from scrapy.crawler import Crawler
# from scrapy import log,signals
from scrapy.settings import Settings
from twisted.internet import reactor
from BzProject.spiders.com.bz.client.BzClient import BzClient
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
import os
from scrapy.cmdline import execute
import time
import threading
from subprocess import Popen
import subprocess
from BzProject.spiders.com.wy.WyCloudMusic import WyCloudMusic

class StartSpider(object):

    def doCmd(self):
        bzSpilder = BzClient()
        settings = get_project_settings()
        os.environ['SCRAPY_SETTINGS_MODULE'] = 'BzProject.settings'
        setting_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
        settings.setmodule(setting_module_path, priority='project')
        # runner = CrawlerRunner(settings)
        # runner.crawl(bzSpilder)
        # reactor.run()
        crawler = CrawlerProcess(settings)#多线程时会报错  signal only works in main thread
        crawler.crawl(bzSpilder)
        crawler.start()

    #解决点击按钮卡死问题
    def sbProcess(self):
        subprocess.Popen("scrapy crawl dk")

    #开始网易云
    def startWyCloudMusicSpider(self):
        wySpilder=WyCloudMusic()
        settings = get_project_settings()
        os.environ['SCRAPY_SETTINGS_MODULE'] = 'BzProject.settings'
        setting_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
        settings.setmodule(setting_module_path, priority='project')
        # runner = CrawlerRunner(settings)
        # runner.crawl(bzSpilder)
        # reactor.run()
        crawler = CrawlerProcess(settings)  # 多线程时会报错  signal only works in main thread
        crawler.crawl(wySpilder)
        crawler.start()

if __name__=="__main__":
    ss=StartSpider()
    ss.startWyCloudMusicSpider()
    #测试地址 https://search.bilibili.com/all?keyword=Legal%20V&from_source=banner_search&spm_id_from=333.334.b_62616e6e65725f6c696e6b.4

