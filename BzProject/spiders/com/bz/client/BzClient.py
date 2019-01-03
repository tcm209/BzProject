#-*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import sys
import io
import json
from scrapy.selector import Selector
# from BzProject.spiders.com.bz.JsonUtils import JsonUtils
from BzProject.spiders.com.bz.LogManager import LogManager
from BzProject.spiders.com.bz.DbHelpers import DbHelpers
from BzProject.spiders.com.bz.client.BzClientUtils import BzClientUtils
import time

class BzClient(scrapy.Spider):
    name = 'dk'
    hostURL='https://search.bilibili.com/all?keyword=米仓凉子'
    #设置访问地址
    allowed_domains = ["bilibili.com",
                       "api.bilibili.com"
                       ]
    #搜索读取页面短视频
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'LIVE_BUVID=AUTO4815398368215790; stardustvideo=1; buvid3=743783AE-1151-4D43-B771-351B5942207F26430infoc; rpdid=kmilsmspoqdosklqkmkxw; fts=1539837710; CURRENT_FNVAL=16; sid=9ngxiviv; UM_distinctid=167069eb3c82b-097390cdbf4e2b-594c2a16-1fa400-167069eb3ca73c; _uuid=1B5AED77-A4E9-C0B1-D117-FE813BA000EC91959infoc',
        'Host': 'search.bilibili.com',
        'Referer': 'https://www.bilibili.com/?',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Upgrade-Insecure-Requests':1,

    }
    #翻页读取  jsonp数据
    commonsHeaders={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'LIVE_BUVID=AUTO4815398368215790; stardustvideo=1; buvid3=743783AE-1151-4D43-B771-351B5942207F26430infoc; rpdid=kmilsmspoqdosklqkmkxw; fts=1539837710; CURRENT_FNVAL=16; sid=9ngxiviv; UM_distinctid=167069eb3c82b-097390cdbf4e2b-594c2a16-1fa400-167069eb3ca73c',
        'Host': 'api.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Upgrade-Insecure-Requests': 1,

    }

    def __init__(self):
        self.dbtool = DbHelpers()
        self.bzUtils=BzClientUtils()
    #设置baseurl
    def queryReqURL(self):
        rw=self.dbtool.queryOne("select search,keyword,type,barrage from search where status=1")
        print(rw)
        self.keyword=rw[1]
        self.searchval=rw[0]
        self.type=int(rw[2])#小视频 1 影视：0
        self.barrage=int(rw[3])#读取弹幕 ：1 读取评论：0
        self.bzUtils.writeLog("查询要爬取的地址"+self.searchval+"关键字"+self.keyword)
    #开始读取
    def start_requests(self):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
        self.queryReqURL()
        return [
            Request(self.searchval,callback=self.parseSearch,headers=self.headers)
            # Request(self.baseURL, callback=self.parseSearch, headers=self.headers)
        ]
    def parseSearch(self,response):
        containsElement=response.xpath("//div[@class='result-wrap clearfix']").extract()
        leEle=len(containsElement)
        if leEle!=0:
            if self.type==0:#读取搜索结果存在影视剧下 eg:大鱼海棠
                liItems = response.xpath("//li[@class='synthetical']")
                isExistMv=len(liItems)
                if isExistMv!=0:
                    for item in liItems:
                        avName = item.xpath("div/div[@class='right-info']/div[@class='headline']/a/@title").extract()[
                            0]  # 电视剧名称
                        avMediaURL = \
                        item.xpath("div/div[@class='right-info']/div[@class='headline']/a/@href").extract()[0]  # 播放地址
                        avType = item.xpath("div/div[@class='right-info']/div/span/text()").extract()[0]  # 影视类型
                        avPlayURL = item.xpath("div/div[@class='right-info']/div[@class='headline']/a/@href").extract()[
                            0]
                        # 读取
                        # 播放电影不需要循环第几集
                        ssStartNum = avPlayURL.find("md")
                        ssEndNum = avPlayURL.find("/?")
                        avid = avPlayURL[ssStartNum + 2:ssEndNum]
                        mvHeader = self.bzUtils.getMvHeaders(avPlayURL)
                        mvURL = self.bzUtils.getBangumi_web_api_url_season(avid)
                        yield Request(url=mvURL, callback=self.parseMvPage, headers=mvHeader,meta={"avType": avType, "avBarrage": self.barrage})
                else:
                    print("搜索："+self.keyword+"不存在影视剧")
                    return


            elif self.type==1:#读取搜索下小视频
                # 读取当前页面的视频信息
                liItems = response.xpath('//ul[@class="video-contain clearfix"]//li[@class="video matrix"]')
                # print(liItems)
                # for liItem in liItems:
                #     href = liItem.xpath('a/@href').extract()[0]
                #     title = liItem.xpath('a/@title').extract()[0]
                #     avid = liItem.xpath('div[@class="info"]/div[@class="headline clearfix"]/span[@class="type avid"]/text()')[0].extract()
                #     watchNum = liItem.xpath('div[@class="info"]/div[@class="tags"]/span[@class="so-icon watch-num"]/text()')[0].extract()
                #     # print(watchNum)
                #     upTime = liItem.xpath('div[@class="info"]/div[@class="tags"]/span[@class="so-icon time"]/text()')[0].extract()
                #     upName = liItem.xpath('div[@class="info"]/div[@class="tags"]/span[@class="so-icon"]/a[@class="up-name"]/text()')[0].extract()
                    # print("上传人："+upName+"\t上传时间："+upTime+"\t观看数："+watchNum+"\t视频id："+avid+"\t视频名称："+title+"\t视频地址："+href)
                # 判断是否只存在一页
                pager = response.xpath("//div[@class='page-wrap']//div").extract()
                pnum = len(pager)
                if pnum != 0:
                    # 读取页数
                    currentPage = response.xpath('//ul[@class="pages"]//li[@class="page-item active"]//button[@class="pagination-btn num-btn"]/text()')[0].extract()  # 当前页
                    pageCount = response.xpath('//ul[@class="pages"]//li[@class="page-item last"]//button[@class="pagination-btn"]/text()')[0].extract()  # 总页数
                    self.bzUtils.writeLog("当前页：" + str(currentPage) + "总页数：" + str(pageCount)+"\n")
                    lastPage = int(pageCount) + 1
                    for i in range(1,lastPage):
                        nextPageUrl="https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword="+str(self.keyword)+"&page="+str(i)
                        yield Request(url=nextPageUrl, callback=self.parseNextPage, headers=self.commonsHeaders,meta={"avBarrage":self.barrage})
                        self.bzUtils.writeLog("搜索结果存在多页\t" + nextPageUrl + "\n")

                else:
                    nextPageUrl = "https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword=" + str(self.keyword) + "&page=1"
                    yield Request(url=nextPageUrl, callback=self.parseNextPage, headers=self.commonsHeaders,meta={"avBarrage":self.barrage})
                    self.bzUtils.writeLog("搜索结果只有一页\t" + nextPageUrl + "\n")

        else:
            self.bzUtils.writeLog("搜索结果为空")



    #读取电影页面电影信息
    def parseMvPage(self,response):
        avType=response.meta['avType']
        avBarrage=response.meta['avBarrage']
        html = response.text
        # data =unicode_str(html)
        jsonData = json.loads(html)

        movieArr=self.bzUtils.movieDetails(jsonData,avType)
        oidArr =movieArr[0]
        cidArr=movieArr[1]
        if avBarrage == 1:#读取弹幕
            for cid in cidArr:
                barrageURL=self.bzUtils.getBarrageURL(cid)
                barrageHeader=self.bzUtils.getBarrageHeader()
                yield Request(url=barrageURL, headers=barrageHeader, callback=self.parseBarrage)

        elif avBarrage == 0:#读取评论
            for oid in oidArr:
                directURL = self.bzUtils.getReplayURL(oid)
                yield Request(url=directURL, headers=self.commonsHeaders, callback=self.parseReplyVideo,meta={"oid": str(oid)})


    #
    # 第一个参数是弹幕出现的时间
    # 以秒数为单位。
    # 第二个参数是弹幕的模式1..3
    # 滚动弹幕4
    # 底端弹幕5
    # 顶端弹幕6.
    # 逆向弹幕7
    # 精准定位8
    # 高级弹幕
    # 第三个参数是字号， 12
    # 非常小, 16
    # 特小, 18
    # 小, 25
    # 中, 36
    # 大, 45
    # 很大, 64
    # 特别大
    # 第四个参数是字体的颜色
    # 以HTML颜色的十位数为准
    # 第五个参数是Unix格式的时间戳。基准时间为
    # 1970 - 1 - 1
    # 0
    # 8: 00:00
    # 第六个参数是弹幕池0
    # 普通池 1
    # 字幕池2
    # 特殊池 【目前特殊池为高级弹幕专用】
    # 第七个参数是发送者的ID，用于“屏蔽此弹幕的发送者”功能
    # 第八个参数是弹幕在弹幕数据库中rowID 用于“历史弹幕”功能
    def parseBarrage(self,response):
        dItems=response.xpath("//d")
        chatid=response.xpath("//chatid/text()").extract()[0]
        self.bzUtils.addBarrageData(dItems,chatid)


    #进入
    def parseNextPage(self,response):
        avBarrage = response.meta['avBarrage']
        html = response.text
        jpJson = json.loads(html)
        data=jpJson['data']
        numPages=data['numPages']
        numResults=data['numResults']
        page=data['page']
        pageSize=data['pagesize']
        seid=data['seid']
        showColumn=data['show_column']
        result=data['result']

        dic=self.bzUtils.readVideo(result)
        #遍历dict  字典key=cid
        for key in dic:
            if avBarrage == 1:
                self.bzUtils.writeLog("读取弹幕\n")
                directHeader=self.bzUtils.getViewHeader()
                directURL=self.bzUtils.getViewURL(str(key))
                yield Request(url=directURL,headers=directHeader,callback=self.parseBarrageVideo)
            else:
                self.bzUtils.writeLog("读取评论\n")
                directURL = "https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid=" + str(key)
                yield Request(url=directURL, headers=self.commonsHeaders, callback=self.parseReplyVideo,meta={"oid": str(key)})


    #读取详细信息
    def parseBarrageVideo(self,response):
        html = response.text
        jsonData = json.loads(html)
        code=jsonData['code']
        message=jsonData['message']
        data=jsonData['data']
        cidArr=self.bzUtils.addViewData(data)
        for cid in cidArr:
            barrageURL = self.bzUtils.getBarrageURL(cid)
            barrageHeader = self.bzUtils.getBarrageHeader()
            yield Request(url=barrageURL, headers=barrageHeader, callback=self.parseBarrage)

    #小视频播放页面
    def parseReplyVideo(self,response):
        oid=response.meta['oid']
        html = response.text
        dataJSON = json.loads(html)
        dataPage = dataJSON['data']['page']
        pageCount =self.bzUtils.getReplyPageCount(dataPage)
        self.bzUtils.writeLog("总页数："+str(pageCount))
        # for pn in range(1,pageCount+1):
        for pn in range(1, pageCount+1):
            pnURL = "https://api.bilibili.com/x/v2/reply?pn=" + str(pn) + "&type=1&oid=" + str(oid) + "&sort=0";
            # self.bzUtils.writeLog("视频播放页 评论翻页\t" + pnURL + "\n")
            yield Request(pnURL, callback=self.parseAnswer, headers=self.commonsHeaders)

    #读取评论
    def parseAnswer(self, response):
        html = response.text
        dataJSON = json.loads(html)
        data = dataJSON["data"]['replies']
        dataHot = dataJSON['data']['hots']
        dataPage = dataJSON['data']['page']
        if data is not None:
            arr = self.bzUtils.getReplys(dataHot)
            print(arr)
            arrLen = len(arr)
            if arrLen != 0:
                for replyURL in arr:
                    yield Request(replyURL, callback=self.parseReplyReply, headers=self.commonsHeaders)
        else:
            self.bzUtils.writeLog("parseComments评论data为空\n")



    def parseReplyReply(self, response):
        # 读取回复评论内的json
        html = response.text
        dataJSON = json.loads(html)
        data = dataJSON["data"]['replies']
        self.bzUtils.getReplys(data)








