#-*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import sys
import io
import json
from scrapy.selector import Selector
from BzProject.spiders.com.bz.JsonUtils import JsonUtils
from BzProject.spiders.com.bz.LogManager import LogManager

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

    log =JsonUtils()

    def start_requests(self):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
        return [
            Request(self.hostURL,callback=self.parseSearch,headers=self.headers)
        ]
    def parseSearch(self,response):
        # html=Selector(text=response)

        avName = response.xpath("//div[@class='right-info']//div[@class='headline']//a/text()").extract()[0]  # 电视剧名称
        #读取当前页面的视频信息
        liItems=response.xpath('//ul[@class="video-contain clearfix"]//li[@class="video matrix"]')
        # print(liItems)
        for liItem in liItems:
            href=liItem.xpath('a/@href').extract()[0]
            title=liItem.xpath('a/@title').extract()[0]
            avid=liItem.xpath('div[@class="info"]/div[@class="headline clearfix"]/span[@class="type avid"]/text()')[0].extract()
            watchNum=liItem.xpath('div[@class="info"]/div[@class="tags"]/span[@class="so-icon watch-num"]/text()')[0].extract()
            # print(watchNum)
            upTime=liItem.xpath('div[@class="info"]/div[@class="tags"]/span[@class="so-icon time"]/text()')[0].extract()
            upName=liItem.xpath('div[@class="info"]/div[@class="tags"]/span[@class="so-icon"]/a[@class="up-name"]/text()')[0].extract()
            # print("上传人："+upName+"\t上传时间："+upTime+"\t观看数："+watchNum+"\t视频id："+avid+"\t视频名称："+title+"\t视频地址："+href)

        #读取页数
        currentPage=response.xpath('//ul[@class="pages"]//li[@class="page-item active"]//button[@class="pagination-btn num-btn"]/text()')[0].extract()#当前页
        pageCount=response.xpath('//ul[@class="pages"]//li[@class="page-item last"]//button[@class="pagination-btn"]/text()')[0].extract()#总页数
        print("当前页："+str(currentPage)+"总页数："+str(pageCount))
        #翻页读取jsonp   https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword=%E7%B1%B3%E4%BB%93%E5%87%89%E5%AD%90&page=2
        testURL="https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword=%E7%B1%B3%E4%BB%93%E5%87%89%E5%AD%90&page=2"
        arr=[]
        lastPage=int(pageCount)+1
        for i in range(1,2):
            nextPageUrl="https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword=米仓凉子&page="+str(i)

            yield Request(url=nextPageUrl, callback=self.parseNextPage, headers=self.commonsHeaders, )
            JsonUtils.writeLog(self.log, "搜索页面\t" + nextPageUrl + "\n")
            # arr.append(nextPageUrl)
        #翻页



        # print("当前页数："+str(currentPage)+"总页数："+str(pageCount))
        print(avName)
    def parseNextPage(self,response):
        print("进入下一页")
        html = response.text
        # data =unicode_str(html)
        jpJson = json.loads(html)
        data=jpJson['data']
        numPages=data['numPages']
        numResults=data['numResults']
        page=data['page']
        pageSize=data['pagesize']
        seid=data['seid']
        showColumn=data['show_column']
        result=data['result']

        dic=JsonUtils.readNextPage(result)
        #遍历dict  字典
        for key in dic:

            directURL="https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid="+str(key)
            # JsonUtils.writeLog(self.log, "视频播放页\t" + directURL + "\n")
            # yield Request(url=directURL,headers=self.commonsHeaders,callback=self.parseShowMV,meta={"oid":str(key)})





        #读取视频内的评论 点击链接https://www.bilibili.com/video/av37883934?from=search&seid=12432765326948362471
        #https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid=37883934
        #翻页 https://api.bilibili.com/x/v2/reply?pn=2&type=1&oid=3383064
        #测试地址 https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid=3383064
        followURL="https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid=9908889"
        yield Request(url=followURL,headers=self.commonsHeaders,callback=self.parseShowMV,meta={"oid":"9908889"})

    #视频播放页面
    def parseShowMV(self,response):
        oid=response.meta['oid']
        html = response.text
        dataJSON = json.loads(html)

        dataPage = dataJSON['data']['page']
        pageCount =JsonUtils.getPageCount(dataPage)
        print("总页数："+str(pageCount))
        # for pn in range(1,pageCount+1):
        for pn in range(1, pageCount+1):
            pnURL = "https://api.bilibili.com/x/v2/reply?pn=" + str(pn) + "&type=1&oid=" + str(oid) + "&sort=0";
            JsonUtils.writeLog(self.log, "视频播放页 评论翻页\t" + pnURL + "\n")
            yield Request(pnURL, callback=self.parseComments, headers=self.commonsHeaders)
            print("测试页码地址："+pnURL)
    #读取评论
    def parseComments(self, response):
        html = response.text
        dataJSON = json.loads(html)
        data = dataJSON["data"]['replies']
        dataHot = dataJSON['data']['hots']
        dataPage = dataJSON['data']['page']
        ju=JsonUtils()
        arr=JsonUtils.getComments(ju,data)
        print(arr)
        arrLen=len(arr)
        if arrLen!=0:
            for replyURL in arr:
                print("请求地址："+replyURL)
                yield Request(replyURL, callback=self.parseReply, headers=self.commonsHeaders)

    def parseReply(self, response):
        # 读取回复评论内的json
        html = response.text
        dataJSON = json.loads(html)
        data = dataJSON["data"]['replies']
        ju = JsonUtils()
        JsonUtils.getComments(ju, data)








