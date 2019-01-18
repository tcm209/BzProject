# -*- coding: utf-8 -*-
from BzProject.spiders.com.wy.WyCloudMusicUtils import WyCloudMusicUtils
import scrapy
from scrapy.http import Request
import json
import base64
import requests
from BzProject.spiders.com.RedisTools import RedisTools

class WyCloudMusic(scrapy.Spider):

    name="wy"

    allowed_domains=[
        'music.163.com'
    ]

    def __init__(self):
        # {playlist: "A_PL_0_", dj: "A_DJ_1_", program: "A_DJ_1_", album: "R_AL_3_", song: "R_SO_4_"};
        #获取工具类
        self.wyutils=WyCloudMusicUtils()
        self.discoverURL=self.wyutils.getDiscoverURL()
        self.header=self.wyutils.getDiscoverHeader()
        self.r=RedisTools().get_redis()

    def start_requests(self):

        # 歌词参数"{id:\"26326159\", lv:\"-1\", tv:\"-1\", csrf_token:\"\"}"
        songid= bytes.decode(self.r.get("keyword"))
        csrftype= str(bytes.decode(self.r.get("type")))
        print("查询类型："+csrftype)
        params = self.wyutils.get_paramsSong(1, str(csrftype), songid)
        encSecKey = self.wyutils.get_encSecKeySong()
        data = {
            "params": params,
            "encSecKey": encSecKey
        }
        # response = requests.post(self.wyutils.getLyricRUL(), headers=self.wyutils.getHeaderSong(), data=data)
        # self.answerLyric(response.content)#不适应scrapy
        #

        if csrftype=="1":#评论
            print("返回执行评论")
            playsongurl = self.wyutils.get_r_so_url(songid)
            return [
                scrapy.FormRequest(playsongurl, headers=self.wyutils.getHeaderSong(), formdata=data,callback=self.parse_csrf_next_page, meta={"url": playsongurl})
                # Request(url= self.wyutils.getDiscoverURL(),headers=self.wyutils.getDiscoverHeader(),callback=self.parseDiscover)#爬取热门
            ]
        elif csrftype=="0":
            print("执行歌词查询")
            return [
                scrapy.FormRequest(self.wyutils.getLyricRUL(), headers=self.wyutils.getHeaderSong(), formdata=data,
                                   callback=self.parseLyric, meta={"crsftype": csrftype})
                # Request(url= self.wyutils.getDiscoverURL(),headers=self.wyutils.getDiscoverHeader(),callback=self.parseDiscover)#爬取热门
            ]




    def parseDiscover(self,response):
        hotCat=response.xpath("//div[@class='n-rcmd']//div[@class='v-hd2']/a/text()").extract()[0]#热门推荐
        hotCatURL=response.xpath("//div[@class='n-rcmd']//div[@class='v-hd2']/a/@href").extract()[0]#热门推荐地址
        print(hotCat)
        hyCat = response.xpath("//div[@class='n-rcmd']//div[@class='v-hd2']//div[@class='tab']/a/text()").extract()[0]  # 华语
        lxCat =response.xpath("//div[@class='n-rcmd']//div[@class='v-hd2']//div[@class='tab']/a/text()").extract()[1]   # 流行
        ygCat = response.xpath("//div[@class='n-rcmd']//div[@class='v-hd2']//div[@class='tab']/a/text()").extract()[2]  # 摇滚
        myCat = response.xpath("//div[@class='n-rcmd']//div[@class='v-hd2']//div[@class='tab']/a/text()").extract()[3]  # 民谣
        dzCat = response.xpath("//div[@class='n-rcmd']//div[@class='v-hd2']//div[@class='tab']/a/text()").extract()[4]  # 电子
        print(hyCat)
        #热门推荐
        liItems = response.xpath("//div[@class='n-rcmd']//ul[@class='m-cvrlst f-cb']//li")
        for liItem in liItems:
            songsheetURL=liItem.xpath("p[@class='dec']/a/@href").extract()[0]#具体歌单地址
            songsheetID=liItem.xpath("p[@class='dec']/a/@data-res-id").extract()[0]#歌单ID
            songsheetTitle=liItem.xpath("p[@class='dec']/a/text()").extract()[0]#歌单标题
            newsongsheetTitle=songsheetTitle.encode("gbk", 'ignore').decode("gbk", "ignore")
            print("歌单地址："+songsheetURL+"\t歌单ID："+str(songsheetID)+"\t 歌单标题："+newsongsheetTitle+"\n")
            #进入热门推荐 歌单内具体歌去

            #暂时出去电台
            ind=songsheetURL.find("dj")
            if ind==-1:
                #读取歌单
                print(songsheetURL)
                # yield Request(url=self.wyutils.getBaseURL() + songsheetURL, headers=self.wyutils.getDiscoverHeader(),callback=self.parseHotRecommend,meta={"APL":songsheetID})
                #热门推荐评论https://music.163.com/weapi/v1/resource/comments/A_PL_0_2542133934?csrf_token=
                # yield Request(url=)
        #测试评论获取
        yield Request(url=self.wyutils.getBaseURL() + "/playlist?id=924680166", headers=self.wyutils.getDiscoverHeader(),
                      callback=self.parseHotRecommend, meta={"APL": "924680166"})
        #新碟上架


        #榜单
        blkBsCat=response.xpath("//div[@id='top-flag']//dl")[0]#飙升
        blkXgCat=response.xpath("//div[@id='top-flag']//dl")[1]#新歌
        blkYcCat = response.xpath("//div[@id='top-flag']//dl")[2]#原创
        # self.wyutils.getTop10PlayMessage(blkBsCat)
        #搜索歌曲'{hlpretag:"<span class="s-fc7">",hlposttag:"</span>",s:"知",type:"1",offset:"0",total:"true",limit:"30",csrf_token:""}'





    #热门推荐
    def parseHotRecommend(self,response):
        APL=response.meta['APL']
        imglogo=response.xpath("//div[@class='g-wrap6']//div[@class='m-info f-cb']//div[@class='cover u-cover u-cover-dj']//img/@data-src").extract()[0]#歌单封面图片
        cntcElement=response.xpath("//div[@class='g-wrap6']//div[@class='m-info f-cb']//div[@class='cntc']")
        title=cntcElement.xpath("//div[@class='hd f-cb']//div//h2/text()").extract()[0]#歌单title
        userface=cntcElement.xpath("//div[@class='user f-cb']//a/@href").extract()[0]#作者头像
        username=cntcElement.xpath("//div[@class='user f-cb']//span[@class='name']//a[@class='s-fc7']/text()").extract()[0]#创建人名称
        usercreatetime=cntcElement.xpath("//div[@class='user f-cb']//span[@class='time s-fc4']/text()").extract()[0]#创建话题时间
        #播放量信息
        fav=cntcElement.xpath("//div[@class='btns f-cb']//a[@class='u-btni u-btni-fav ']//i/text()").extract()[0]#收藏
        share=cntcElement.xpath("//div[@class='btns f-cb']//a[@class='u-btni u-btni-share ']//i/text()").extract()[0]#分享
        cmmt=cntcElement.xpath("//div[@class='btns f-cb']//a[@class='u-btni u-btni-cmmt ']//i//span/text()").extract()[0]#评论
        #标签
        aitems=cntcElement.xpath("//div[@class='tags f-cb']//a")#标签
        tags=""
        for aitem in aitems:
            tag=aitem.xpath("i/text()").extract()[0]
            tags=tags+","+tag
        #介绍
        information=",".join(cntcElement.xpath("//p/text()").extract())#介绍
        print("介绍："+information.encode("gbk", 'ignore').decode("gbk", "ignore"))

        #歌曲列表
        songsElement=response.xpath("//div[@class='g-wrap6']//div[@class='n-songtb']")
        songcount=songsElement.xpath("//div[@class='u-title u-title-1 f-cb']//span[@class='sub s-fc3']//span/text()").extract()[0]#歌曲总数
        playcount=songsElement.xpath("//div[@class='u-title u-title-1 f-cb']//div[@class='more s-fc3']//strong/text()").extract()[0]#播放次数
        # 歌曲列表
        liItems = songsElement.xpath("//div[@id='song-list-pre-cache']//ul[@class='f-hide']//li")
        playArr = self.wyutils.getPlayMusicHotRecommend(liItems)  # 读取歌曲播放地址

        # 读取歌单评论
        urlAPL=self.wyutils.getAPLURLSong(APL)
        #读取播放列表下的评论
        pagenum=int("1")
        params = self.wyutils.get_paramsSong(pagenum,"1",None)
        encSecKey =self.wyutils.get_encSecKeySong()
        data={
            "params": params,
            "encSecKey": encSecKey
        }
        # yield scrapy.FormRequest(url=urlAPL,method="POST",headers=self.wyutils.getHeaderSong(),formdata=data,callback=self.parseAPLAnswer)
        # yield Request(url=urlAPL,headers=self.wyutils.getHeaderSong(),body=data,callback=self.parseAPLAnswer)
        response=requests.post(url=urlAPL, headers=self.wyutils.getHeaderSong(), data=data)
        self.csrf_next_page(response,urlAPL)#读取翻页


        # #读取具体歌曲的评论
        for pyURL in playArr:
            songIDStartNum = int(pyURL.find("id="))
            songIDLen = len(pyURL)
            songID = pyURL[songIDStartNum + 3:songIDLen]
            playsongurl = self.wyutils.get_r_so_url(songID)
            self.answerCsrf(playsongurl, data)


    def answerCsrf(self,url,data):
        response_r_so = requests.post(url=url, headers=self.wyutils.getHeaderSong(), data=data)
        self.csrf_next_page(response_r_so,url)

    #读取评论 翻页
    def csrf_next_page(self,response,urlAPL):
        # 计算总页数
        pagenum = self.answerAPL(response.content,urlAPL)
        pagenum = self.wyutils.calcuPageNum(pagenum)
        if pagenum > 1:
            print("大于1页需要分页读取评论")
            for p in range(2, pagenum + 1):  # 从第二页开始

                print("当前页数：" + str(p) + "\n")
                pParams = self.wyutils.get_paramsSong(p, "1", None)
                pEncSecKey = self.wyutils.get_encSecKeySong()
                pdata = {
                    "params": pParams,
                    "encSecKey": pEncSecKey
                }
                responseAnswer = requests.post(url=urlAPL, headers=self.wyutils.getHeaderSong(), data=pdata)
                self.answerAPL(responseAnswer.content,urlAPL)

    #解析评论response
    def answerAPL(self,json_text,playurl):
        j_text = str(json_text, encoding="utf8")
        json_dict = json.loads(j_text)
        code=json_dict['code']
        total=json_dict['total']
        isMusician=json_dict['isMusician']
        more=json_dict['more']
        #翻页时不存在热评
        # moreHot=json_dict['moreHot']
        topComments=json_dict['topComments']
        userId=json_dict['userId']
        comments=json_dict['comments']
        self.wyutils.crsf_comments(comments,playurl)
        pagenum=int(total)
        return pagenum

    #
    #
    def answerLyric(self,text):
        print("测试")
        print(text)
        j_text = str(text, encoding="utf8")
        json_dict = json.loads(j_text)
        code = json_dict['code']
        lyrictxt = json_dict['lrc']['lyric']
        print(lyrictxt)

    #scrapyform
    def parse_csrf_next_page(self,response):
        urlAPL=response.meta['url']
        # 计算总页数
        pagenum = self.get_page_num(response.text, urlAPL)
        pagenum = self.wyutils.calcuPageNum(pagenum)
        if pagenum > 1:
            print("大于1页需要分页读取评论")
            for p in range(2, pagenum + 1):  # 从第二页开始

                print("当前页数：" + str(p) + "\n")
                pParams = self.wyutils.get_paramsSong(p, "1", None)
                pEncSecKey = self.wyutils.get_encSecKeySong()
                pdata = {
                    "params": pParams,
                    "encSecKey": pEncSecKey
                }
                responseAnswer = requests.post(url=urlAPL, headers=self.wyutils.getHeaderSong(), data=pdata)
                self.answerAPL(responseAnswer.content, urlAPL)

    def get_page_num(self,j_text,playurl):

        json_dict = json.loads(j_text)
        code = json_dict['code']
        total = json_dict['total']
        isMusician = json_dict['isMusician']
        more = json_dict['more']
        # 翻页时不存在热评
        # moreHot=json_dict['moreHot']
        topComments = json_dict['topComments']
        userId = json_dict['userId']
        comments = json_dict['comments']
        self.wyutils.crsf_comments(comments, playurl)
        pagenum = int(total)
        return pagenum


    #scrapy.RequestForm 读取的
    def parseLyric(self,response):
        r_text = response.text
        json_dict = json.loads(r_text)
        crsftype=response.meta['crsftype']
        code = str(json_dict['code'])
        if code=="200":
            param=[]
            lyrictxt = json_dict['lrc']['lyric']
            param.append(lyrictxt)
            self.wyutils.execute_lyric(param)
        else:
            print("不存在歌词")
































