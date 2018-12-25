#-*- coding: utf-8 -*-
from scrapy.crawler import Crawler
# from scrapy import log,signals
from scrapy.settings import Settings
from twisted.internet import reactor
from BzProject.spiders.com.bz.client.BzClient import BzClient
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os


class StartSpider(object):

    def doCmd(self):
        bzSpilder = BzClient()
        settings = get_project_settings()
        os.environ['SCRAPY_SETTINGS_MODULE'] = 'BzProject.settings'
        setting_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
        settings.setmodule(setting_module_path, priority='project')
        crawler = CrawlerProcess(settings)

        crawler.crawl(bzSpilder)
        crawler.start()
        # log.start(loglevel=log.INFO)
        reactor.run()

if __name__=="__main__":
    ss=StartSpider()
    ss.doCmd()

