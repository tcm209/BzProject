# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
from BzProject.spiders.com.bz.DbHelpers import DbHelpers
from BzProject.spiders.com.DateTools import DateTools

class WyCloudMusicUtils(object):

    def __init__(self):
        # self.first_param = "{rid:\"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"
        self.dbhelper=DbHelpers()
        self.dateTool=DateTools()
        self.second_param = "010001"
        self.third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        self.forth_param = "0CoJUm6Qyw8W8jud"
        print("初始化工具类")

    #获取首页地址
    def getBaseURL(self):
        url="https://music.163.com"
        return url
    #获取评论
    def getHotRecommendApiUrl(self,hotid):
        host="https://music.163.com/weapi/v1/resource/comments/A_PL_0_"+str(hotid)+"?csrf_token="
        return host
    #获取
    def get_r_so_url(self,songID):
        url="https://music.163.com/weapi/v1/resource/comments/R_SO_4_"+songID+"?csrf_token="
        return url;

    #获取第一个URL
    def getDiscoverURL(self):
        url="https://music.163.com/discover"
        return url
    #获取歌词地址
    def getLyricRUL(self):
        url=self.getBaseURL()+"/weapi/song/lyric?csrf_token="
        return url

    #获取热门推荐 header
    def getDiscoverHeader(self):
        header={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': '_iuqxldmzr_=32; _ntes_nnid=f6d6f2b93a7a86d66d5089867f22a216,1546483116021; _ntes_nuid=f6d6f2b93a7a86d66d5089867f22a216; WM_TID=d7Rx0MyscLhEFBUQEQd4hBMCxg3OUPLE; Province=0590; City=0793; UM_distinctid=16812f8af355-0a5ce8589fef42-58422116-1fa400-16812f8af36c94; vjuids=86bf1431.16812f8daac.0.3f94a85de485; vjlast=1546506525.1546506525.30; NNSSPID=482a922789d6421a9ffd344c01ae3eb7; __gads=ID=ec02424a1178b974:T=1546506466:S=ALNI_MbETf8hLGpEOaU6NFVePumfYQqy0A; vinfo_n_f_l_n3=884225362055b286.1.0.1546506525409.0.1546506543680; JSESSIONID-WYYY=theMyxkZR61Qi9jqZ%2FRlyk3k%2FWpoEZVbliHU0JX7YOs4UqD0mg6TOBXRzSWNCYxW%2FAsWSTHZWS7FTKaFhYnYBf6O8V%5CxUMQfiqoDKxw0DZGM8YHsOWficR9%5CIcIHKV%5CvdWFiDUw8%2FswQr7vKKKy%2BNZeeTepV2F9gg1w%2FjwneVO6e3%2F7y%3A1546568987920; __utma=94650624.1693375539.1546483117.1546483117.1546567188.3; __utmc=94650624; __utmz=94650624.1546567188.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=4Fcd%2BELsBn%2FO7ErpSa9EJ4nuTaFmHTzMno9oZL%2BTH%2BiFiXJVegp0kack7c27o7CYh0vfao0G7Bm2bXzW%2F6Sz3qKCC37Am0O%2FqwXVi3LqBuYaccWNjWcXrsNDi4YxGhqGR24%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed1bc39969dfdd0c77b89ac8eb2d85e939e9f85f23b8292fc88ed52f6e7f7a9e52af0fea7c3b92af89aad85aa4f90ad8e8fae45f59bbe91d26bfb9b86d5ed7f98bf8a8ecb60ba93a290bc659a94e5b5cb21ab9aa7b9c95ea7b9c0d1ea6ba1b5f984b13dade98dbaeb3cb6baaf90b34df59ea3d3e154ba89e1d7d272f1af85a4c239f59fa3d1ce25b3a998b7ec3990af8e96dc6ba1bd99afe95da188be94cd50abec9799c664b3999ed3b737e2a3; __utmb=94650624.4.10.1546567188',
            'Host': 'music.163.com',
            'Referer': 'https://music.163.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        return header
    #获取前十的歌单
    def getTop10PlayMessage(self,cat):
        items=cat.xpath("dd/ol/li")
        for item in items:
            topIndex=item.xpath("span/text()").extract()[0]#第几
            topTitle=item.xpath("a/text()").extract()[0]#歌名
            topplayurl=item.xpath("a/@href").extract()[0]#播放地址
            topplayod=item.xpath("div[@class='oper']/a[@class='s-bg s-bg-11']/@data-res-id").extract()[0]#歌曲播放ID
            print("歌名："+topTitle.encode("gbk", 'ignore').decode("gbk", "ignore")+"播放地址"+topplayurl)

    #解析歌曲列表
    def getPlayMusicHotRecommend(self,items):
        playUArr=[]
        #播放地址：/song?id=256468
        for item in items:
            playurl=item.xpath("a/@href").extract()[0]
            playname=item.xpath("a/text()").extract()[0]
            # print(playname.encode("gbk", 'ignore').decode("gbk", "ignore"))

            #
            playurldetail=self.getBaseURL()+playurl
            print("播放地址：" + playurldetail)
            playUArr.append(playurldetail)
        return playUArr


    #读取评论
    def getAPLURLSong(self,songid):
        url="https://music.163.com/weapi/v1/resource/comments/A_PL_0_"+str(songid)+"?csrf_token="
        return url

    def getHeaderSong(self):
        headers = {
            'Cookie': '_iuqxldmzr_=32; _ntes_nnid=f6d6f2b93a7a86d66d5089867f22a216,1546483116021; _ntes_nuid=f6d6f2b93a7a86d66d5089867f22a216; WM_TID=d7Rx0MyscLhEFBUQEQd4hBMCxg3OUPLE; Province=0590; City=0793; UM_distinctid=16812f8af355-0a5ce8589fef42-58422116-1fa400-16812f8af36c94; vjuids=86bf1431.16812f8daac.0.3f94a85de485; vjlast=1546506525.1546506525.30; __gads=ID=ec02424a1178b974:T=1546506466:S=ALNI_MbETf8hLGpEOaU6NFVePumfYQqy0A; vinfo_n_f_l_n3=884225362055b286.1.0.1546506525409.0.1546506543680; JSESSIONID-WYYY=Uh9fzOoITNp4ub6Y3Tufss1qwMRpKa1TpRk3%2BaPcO3NPUOEZ%2FxkGSEi1683%2BjDZmNEOJp9hIlC0Yg3Ypbc9HE7SZMaOjWxCIsf%5Cd4U6nX7jP%5CU%5C5d1rkDE47bsZPKz639gR6QulHSOehTGF3AdETPJQsBwP%2BI4NXbhfFlx7XA%5CvlrjDU%3A1546825050089; __utma=94650624.1693375539.1546483117.1546590243.1546823250.9; __utmc=94650624; __utmz=94650624.1546823250.9.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=20EurL4SPsfx9DQSm0BS67LUeBfwkhdEsA2nULkNWWbMXrJxJ1GKh48WKpK%2BAcDqv%2FDGe91OdqfG7aNUXmHJvXx5T32SrMD0F1bM%2FNJwU%2FW6xDrHU8aqYcNfcegtLmcnenk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccb2798cb500d3ec418eeb8fb3d54f929f9bbaee6886b8a290bc509a959c94d72af0fea7c3b92af2f08b96f148f88da094e574fb9c9fb4f03c828dfad8cf5fa79eaa98ea64a89bbda2b1669794a5afd65da2939893c9748aef89aceb40fc898591ca2183bd8c92f5258899abdab445a8afaaa8b66b8e8b988ecb42b688b8d6d739f28dbeaec73c86efaeaeae468aa99bd0d63ebc9cbea9d834a3af9784cd6ea1bba995cf67a1b2ab8fea37e2a3; __utmb=94650624.5.10.1546823250',
            'Referer': 'http://music.163.com/',
            'Accept-Language': "zh-CN,zh;q=0.9",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

        }
        return headers

    #获取第一个参数
    #offset =0 评论页数-1
    #total=true  第一页是true 其他均为false
    #limit=20 一页显示20条评论
    #crsftype:0 歌词  1 评论
    def get_fistParam(self,pagenum,crsftype,songid):
        if crsftype == "0":
            first_param = "{id:"+str(songid)+", lv:\"-1\", tv:\"-1\", csrf_token:\"\"}"
        elif crsftype == "1":
            offset = (pagenum - 1)*20
            if pagenum > 1:
                total = "false"
            elif pagenum == 1:  # 第一页时 total设置为true
                total = "true"
            first_param = "{rid:\"\", offset:" + str(offset) + ", total:" + total + ", limit:\"20\", csrf_token:\"\"}"

        return first_param

    def get_paramsSong(self,pagenum,crsftype,songid):
        first_param=self.get_fistParam(pagenum,crsftype,songid)
        iv = "0102030405060708"
        first_key = self.forth_param
        second_key = 16 * 'F'
        h_encText =self.AES_encryptSong(first_param, first_key, iv)
        h_encText =self.AES_encryptSong(h_encText, second_key, iv)
        return h_encText

    def get_encSecKeySong(self):
        encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
        return encSecKey

    def AES_encryptSong(self,text, key, iv):
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        encrypt_text = encryptor.encrypt(text)
        # encrypt_text = base64.b64encode(encrypt_text)
        encrypt_text = str(base64.b64encode(encrypt_text))[2:-1]
        return encrypt_text

    #评论解析
    def crsf_comments(self,datas,playurl):
        sqlArr=[]
        sql="INSERT INTO answerwy(commentId,commentLocationType,content,isRemoveHotComment,liked,likedCount,parentCommentId," \
            "pendantData,repliedMark,showFloorComment,status,createtime,authStatus,avatarUrl,expertTags," \
            "experts,locationInfo,nickname,remarkName,userId,userType,vipType,playurl)" \
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for item in datas:
            params=[]
            beReplied=item['beReplied']
            commentId=item['commentId']
            commentLocationType=item['commentLocationType']
            content=item['content']#内容
            decoration=item['decoration']
            expressionUrl=item['expressionUrl']
            isRemoveHotComment=item['isRemoveHotComment']
            liked=item['liked']
            likedCount=item['likedCount']
            parentCommentId=item['parentCommentId']
            pendantData = item['pendantData']
            if pendantData is not None:
                pendantData = item['pendantData']['imageUrl']

            repliedMark=item['repliedMark']
            showFloorComment=item['showFloorComment']
            status=item['status']
            timeint=item['time']
            time_str=self.dateTool.get_convertdate(timeint)
            #用户详细信息
            authStatus=item['user']['authStatus']
            avatarUrl = item['user']['avatarUrl']
            expertTags = item['user']['expertTags']
            usertags=None
            if expertTags is not None:
                lenTag = len(expertTags)
                if lenTag != 0:
                    usertags=','.join(expertTags)
            experts = item['user']['experts']#dict
            expertsstr=""
            if experts is not None:
                for val in experts.values():
                    expertsstr=expertsstr+val+","



            locationInfo = item['user']['locationInfo']
            nickname = item['user']['nickname']
            remarkName = item['user']['remarkName']
            userId = item['user']['userId']
            userType = item['user']['userType']
            # vipRights = item['user']['vipRights']
            vipType = item['user']['vipType']
            #参数
            params.append(commentId)
            params.append(commentLocationType)
            params.append(content)
            params.append(isRemoveHotComment)
            params.append(liked)
            params.append(likedCount)
            params.append(parentCommentId)
            params.append(pendantData)
            params.append(repliedMark)
            params.append(showFloorComment)
            params.append(status)
            params.append(time_str)
            params.append(authStatus)
            params.append(avatarUrl)
            params.append(usertags)
            params.append(expertsstr)
            params.append(locationInfo)
            params.append(nickname)
            params.append(remarkName)
            params.append(userId)
            params.append(userType)
            # params.append(vipRights)
            params.append(vipType)
            params.append(playurl)
            sqlArr.append(params)
            print("评论"+content.encode("gbk", 'ignore').decode("gbk", "ignore"))

        self.dbhelper.executeSqlMany(sql, sqlArr)


    #计算页数 一页显示20条
    def calcuPageNum(self,totalpage):
        size=20
        pageInt=totalpage//size
        pageFloat=totalpage/size
        pageNum=pageInt

        if pageFloat>pageInt:#存在余数
            pageNum=pageInt+1
        elif pageFloat<1:#仅仅只有一页
            pageNum=1

        print("总页数"+str(pageNum))
        return pageNum

    #新增数据到歌词表
    def execute_lyric(self,param):
        self.dbhelper.executeSql("insert into lyricwy(context)VALUES (%s)",param)






