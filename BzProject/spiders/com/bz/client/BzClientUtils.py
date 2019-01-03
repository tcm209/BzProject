from BzProject.spiders.com.bz.DbHelpers import DbHelpers
import time
class BzClientUtils(object):

    def __init__(self):
        self.dbHelper=DbHelpers()
        self.baseURL = "https://www.bilibili.com/"
        self.apiURL="https://api.bilibili.com/x/v2/reply"
        self.oidArr=[]
        self.cidArr=[]
        # 存放评论下的讨论内容
        self.nextArr = []
        self.answerArr = []

    #视频播放页面 请求header
    def getMvHeaders(self,referURL):
        headers={
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'buvid3=59D37C8D-70E3-437B-B1A0-6E01AADA58C985515infoc; LIVE_BUVID=AUTO9315458908042917; fts=1545891194; sid=ldaaqzae',
            'Host': 'bangumi.bilibili.com',
            'Origin': 'https://www.bilibili.com',
            'Referer':referURL,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Upgrade-Insecure-Requests': 1,
        }
        return headers
    #
    def getBangumi_web_api_url(self,avid):
        host="https://bangumi.bilibili.com/ext/web_api/season_count?season_id="+str(avid)+"&season_type=2"
        return host
    #影视播放页面
    def getBangumi_web_api_url_season(self,avid):
        host="https://bangumi.bilibili.com/view/web_api/season?media_id="+str(avid)
        return host

    #读取视频播放页面回复的url json格式
    def getReplayURL(self,oid):
        host="https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid="+str(oid)
        return host
    #弹幕获取地址
    def getBarrageURL(self,cid):
        host="https://api.bilibili.com/x/v1/dm/list.so?oid="+str(cid)
        return host
    #读取小视频详细资料
    def getViewURL(self,cid):
        host="https://api.bilibili.com/x/web-interface/view?aid="+str(cid)
        return host
    #读取视频详细地址header
    def getViewHeader(self):
        header={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection': 'keep-alive',
            'Cookie':'buvid3=59D37C8D-70E3-437B-B1A0-6E01AADA58C985515infoc; LIVE_BUVID=AUTO9315458908042917; fts=1545891194; rpdid=kmilsmspoqdospslqooiw; stardustvideo=1; CURRENT_FNVAL=16; sid=8r3ms873',
            'Host': 'api.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Upgrade-Insecure-Requests': 1,
        }
    #弹幕请求header
    def getBarrageHeader(self):
        timeStr=time.ctime()
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'api.bilibili.com',
            'If-Modified-Since':timeStr,
            'Origin': 'https://www.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        return headers
    #播放页面  读取视频信息
    def addViewData(self,data):
        cidArr=[]
        params=[]
        aid=data['aid']
        attribute=data['attribute']
        cid=data['cid']
        copyright=data['copyright']
        ctime=data['ctime']
        desc=data['desc']
        duration=data['duration']
        dynamic=data['dynamic']
        no_cache=data['no_cache']
        face=data['owner']['face']
        mid=data['owner']['mid']
        name=data['owner']['name']
        pubdate=data['pubdate']
        coin=data['stat']['coin']
        danmaku=data['stat']['danmaku']
        dislike=data['stat']['dislike']
        favorite=data['stat']['favorite']
        his_rank=data['stat']['his_rank']
        like=data['stat']['like']
        now_rank=data['stat']['now_rank']
        reply=data['stat']['reply']
        share=data['stat']['share']
        view=data['stat']['view']
        state=data['state']
        tid=data['tid']
        title=data['title']
        tname=data['tname']
        videos=data['videos']
        params.append(aid)
        params.append(attribute)
        params.append(cid)
        params.append(copyright)
        params.append(ctime)
        params.append(desc)
        params.append(duration)
        params.append(dynamic)
        params.append(no_cache)
        params.append(face)
        params.append(mid)
        params.append(name)
        params.append(pubdate)
        params.append(coin)
        params.append(danmaku)
        params.append(dislike)
        params.append(favorite)
        params.append(his_rank)
        params.append(like)
        params.append(now_rank)
        params.append(reply)
        params.append(share)
        params.append(view)
        params.append(state)
        params.append(tid)
        params.append(title)
        params.append(tname)
        params.append(videos)
        sql="INSERT INTO videoview(aid,attribute,cid,copyright,ctime,descv,duration," \
            "dynamic,no_cache,face,mid,name_v,pubdate,coin,danmaku,dislike,favorite," \
            "his_rank,like_v,now_rank,reply,share,view_v,state,tid,title,tname,videos)VALUES " \
            "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.dbHelper.executeSql(sql,params)
        cidArr.append(cid)
        return cidArr


    #保存弹幕
    def addBarrageData(self,dItems,chartid):
        sqlArr=[]
        for dItem in dItems:
            params=[]
            text=dItem.xpath('text()').extract()[0]
            pdatas=dItem.xpath('@p').extract()[0]
            pArr=pdatas.split(',')
            ptime = pArr[0]  # 弹幕时间
            pms = pArr[1]  # 弹幕模式
            pfontsize = pArr[2]  # 字号
            pfontcolor = pArr[3]  # 字体颜色
            psj = pArr[4]  # 时间戳
            time_local = time.localtime(int(psj))
            createBarrageDt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)#发送弹幕时间
            pBarrage = pArr[5]  # 弹幕池
            puserid = pArr[6]  # 发送者id
            prowid = pArr[7]  # 弹幕rowid

            params.append(ptime)
            params.append(pms)
            params.append(pfontsize)
            params.append(pfontcolor)
            params.append(createBarrageDt)
            params.append(pBarrage)
            params.append(puserid)
            params.append(prowid)
            params.append(text)
            params.append(chartid)
            sqlArr.append(params)
        sql="INSERT INTO barrage(ptime,pms,pfontsize,pfontcolor,createBarrageDt,pBarrage,puserid,prowid,context,chartid)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.dbHelper.executeSqlMany(sql,sqlArr)

    #视频播放页面 影视具体信息
    def movieDetails(self,jsonData,avType):
        #清空下上次塞入的数据
        del self.oidArr[:]
        del self.cidArr[:]

        result = jsonData["result"]
        params = self.getResults(result, avType)
        # sql 新增
        sql = "insert into AVTABLE(actors,alias,evaluate,jp_title,media_id,link,avcount,score,season_id,staff,style,title,total_ep)" \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.dbHelper.executeSql(sql, params)

        # 新增到ep表内
        datas = jsonData["result"]['episodes']
        epSql = "INSERT INTO epview(aid,cid,cover,duration,ep_id,episode_status,fromep," \
                "indexep,index_title,mid,page,pub_real_time,section_id,section_type,vid,refererURL,targetURL)" \
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        epArr = self.getEpisodes(datas)
        epNum = len(epArr)
        if epNum != 0:
            self.dbHelper.executeSqlMany(epSql, epArr)
        else:
            print("不存在")

        return self.oidArr,self.cidArr

    #视频播放页面
    def getResults(self,data,avType):
        paras = []
        actors = data['actors']  # 演员
        alias = data['alias']  # 简称
        evaluate = data['evaluate']  # 简介
        jp_title = data['jp_title']  # 剧名
        media_id = data['media_id']  # 剧ID
        link = data['link']  # 连接地址
        count = data['rating']['count']  # 点评人数
        score = data['rating']['score']  # 评分
        season_id = data['season_id']  # session ID
        staff = data['staff']  # 导演
        styles = data['style']  # 类型
        style = ','.join(str(i) for i in styles)
        title = data['title']  # 剧名
        if avType=="电影":
            total_ep = ""  # 总多少集
        else:
            total_ep=data['total_ep']

        paras.append(actors)
        paras.append(alias)
        paras.append(evaluate)
        paras.append(jp_title)
        paras.append(media_id)
        paras.append(link)
        paras.append(count)
        paras.append(score)
        paras.append(season_id)
        paras.append(staff)
        paras.append(style)
        paras.append(title)
        paras.append(total_ep)
        return paras




    #视频播放页面 影视具体信息 比如第几集
    def getEpisodes(self,datas):
        epArr = []
        for obj in datas:
            epParas = []
            cid = obj['cid']
            cover = obj['cover']
            duration = obj['duration']
            episode_status = obj['episode_status']
            fromid = obj['from']
            index = obj['index']
            index_title = obj['index_title']
            mid = obj['mid']
            pub_real_time = obj['pub_real_time']
            section_id = obj['section_id']
            section_type = obj['section_type']
            vid = obj['vid']
            oid = str(obj['aid'])  # api地址oid
            ep = str(obj['ep_id'])
            pn = str(obj['page'])  # 第几页
            refererURL = self.baseURL + obj['from'] + "/play/ep" + ep + "?from=search"
            targetURL = self.apiURL + "?pn=" + str(pn) + "&type=1&oid=" + str(oid) + "&sort=0"
            #sql新增字段
            epParas.append(oid)
            epParas.append(cid)
            epParas.append(cover)
            epParas.append(duration)
            epParas.append(ep)
            epParas.append(episode_status)
            epParas.append(fromid)
            epParas.append(index)
            epParas.append(index_title)
            epParas.append(mid)
            epParas.append(pn)
            epParas.append(pub_real_time)
            epParas.append(section_id)
            epParas.append(section_type)
            epParas.append(vid)
            epParas.append(refererURL)
            epParas.append(targetURL)
            epArr.append(epParas)#
            #查询评论的id
            self.oidArr.append(oid)
            self.cidArr.append(cid)
        return epArr


    #读取视频
    def readVideo(self, data):
        arr = []
        dict = {}
        for obj in data:
            param = []
            #id=aid
            aid = obj['aid']  # int
            arcrank = obj['arcrank']  # str
            arcurl = obj['arcurl']  # str
            author = obj['author']  # str
            badgepay = obj['badgepay']  # str
            description = obj['description']  # str
            duration = obj['duration']  # str
            favorites = obj['favorites']  # int
            id = obj['id']  # int id=aid
            is_pay = obj['is_pay']  # int
            mid = obj['mid']  # int 作者id
            pic = obj['pic']  # str
            play = obj['play']  # int
            pubdate = obj['pubdate']  # int
            rank_index = obj['rank_index']  # int
            rank_offset = obj['rank_offset']  # int
            rank_score = obj['rank_score']  # int
            review = obj['review']  # int
            senddate = obj['senddate']  # int
            tag = obj['tag']  # str
            title = obj['title']  # str
            type = obj['type']  # str
            typeid = obj['typeid']  # str
            typename = obj['typename']  # str
            video_review = obj['video_review']
            # print("上传人："+author+"描述："+description+"连接地址："+arcurl+"av编号："+str(id))
            dict.__setitem__(id, arcurl)
            param.append(aid)
            param.append(arcrank)
            param.append(arcurl)
            param.append(author)
            param.append(badgepay)
            param.append(description)
            param.append(duration)
            param.append(favorites)
            param.append(id)
            param.append(is_pay)
            param.append(mid)
            param.append(pic)
            param.append(play)
            param.append(pubdate)
            param.append(rank_index)
            param.append(rank_offset)
            param.append(rank_score)
            param.append(review)
            param.append(senddate)
            param.append(tag)
            param.append(title)
            param.append(type)
            param.append(typeid)
            param.append(typename)
            param.append(video_review)
            arr.append(param)
        self.addVideoData(arr)
        return dict

    # 读取视频播放页面总页数
    def getReplyPageCount(self,data):
        pageCount = data['count']  # 全部评论数
        pageNum = data['num']
        pageSize = data['size']
        acount = data['acount']  # 全部评论数+回复数 +删除
        p1 = pageCount / pageSize
        p2 = pageCount // pageSize
        pageAcount = 0
        if p1 > p2:
            pageAcount = p2 + 1
        else:
            pageAcount = p2

        self.writeLog("总页数" + str(acount) + "count：" + str(pageCount) + "一页多少：" + str(pageSize) + " 当前页码：" + str(
            pageNum) + "总页码" + str(pageAcount))
        return pageAcount

    # 读取视频播放页面评论
    def getReplys(self, data):

        # 读取内容前清空数组
        del self.answerArr[:]
        del self.nextArr[:]
        self.commonMethod(data)  # 对数组进行添加数据
        if self.answerArr is not None:
            sql = "insert into answer(rpid,answercount,ctime,floor,answerike,mid,oid,parent," \
                  "rcount,device,message,displayRank,avatar,current_level,uname,rank,sex,sign)" \
                  "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.dbHelper.executeSqlMany(sql, self.answerArr)

        else:
            self.writeLog("数组为空，不执行新增")

        return self.nextArr

    # 公共读取方法
    def commonMethod(self, data):
        for obj in data:
            replies = obj['replies']
            params = self.readDataDetails(obj)
            if params is not None:  # 判断读取到的评论是否为空 或者已经读取过
                ln = len(params)
                if ln != 0:
                    self.answerArr.append(params)

            if replies is None:
                self.writeLog("当前repliesw为空  不执行写入txt操作")
            else:
                self.writeLog("replies不为空")
                j = len(replies)
                self.writeLog("回复数量：" + str(j))
                self.commonMethod(replies)
    # 读取评论
    def readDataDetails(self, obj):
        # 添加list批量新增的字段
        params = []
        rpid = obj['rpid']
        count = obj['count']
        ctime = obj['ctime']
        floor = obj['floor']
        like = obj['like']
        mid = obj['mid']
        oid = obj['oid']
        parent = obj['parent']
        rcount = obj['rcount']  # 回复数 此条评论下回复数量
        # content
        device = obj['content']['device']
        message = obj['content']['message']
        # member
        displayRank = obj['member']['DisplayRank']
        avatar = obj['member']['avatar']
        current_level = obj['member']['level_info']['current_level']

        uname = obj['member']['uname']
        rank = obj['member']['rank']
        sex = obj['member']['sex']
        sign = obj['member']['sign']
        rw = self.queryByRpid(rpid)
        if rw is None:
            # 添加
            params.append(rpid)
            params.append(count)
            params.append(ctime)
            params.append(floor)
            params.append(like)
            params.append(mid)
            params.append(oid)
            params.append(parent)
            params.append(rcount)
            params.append(device)
            params.append(message)
            params.append(displayRank)
            params.append(avatar)
            params.append(current_level)
            params.append(uname)
            params.append(rank)
            params.append(sex)
            params.append(sign)
        else:
            print("当前object为空")

        logTxt = "姓名：" + uname + " rpid：" + str(rpid) + " 回复内容：" + message + "\n"
        self.writeLog(logTxt)
        # 默认评论下讨论只显示前3条
        if rcount > 3:
            print("rowcoutn  是否大于3")
            self.readReplyChilds(rcount, oid, rpid)
        return params

    # 读取评论下的相互评论
    def readReplyChilds(self, rcount, oid, rpid):
        # 读取b站 互相回复
        if rcount > 3:
            pnu = rcount / 10  # 正常除法
            pnum = rcount // 10  # 取整数部分
            pg = 1
            print("pnu: " + str(pnu) + " pnum :" + str(pnum))
            if pnu > pnum:
                if pnu < 1:
                    pnum = 1
                pg = pnum + 1
            else:
                pg = pg + 1
                self.writeLog("相互评论总回复：" + str(pg))
            for i in range(1, pg):

                tarRepliesURL = "https://api.bilibili.com/x/v2/reply/reply?pn="+str(i)+"&type=1&oid=" + str(oid) + "&ps=10&root=" + str(rpid) + ""
                self.writeLog("相互评论："+tarRepliesURL)
                self.nextArr.append(tarRepliesURL)

        if len(self.nextArr) == 0:
            self.writeLog("评论下的相互回复为空，不执行再次读取")
        else:
            self.writeLog("评论下的相互回复为不为空，执行再次读取")

    def writeLog(self, logtxt):
        f = open(r'E:\Pythonwork\BzProject\log\log.txt', 'a+', encoding='utf-8')
        f.write(logtxt)
        f.close()

    # 批量新增
    def addVideoData(self, param):
        # print("=========新增至数据库===========")
        if param is not None:
            sql = "insert into video (aid,arcrank,arcurl,author,badgepay,description,duration,favorites," \
                  "sid,is_pay,mid,pic,play,pubdate,rank_index,rank_offset,rank_score,review,senddate,tag,title,tpe,typeid,typename,video_review)values(%s,%s,%s," \
                  "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.dbHelper.executeSqlMany(sql, param)

    # 查询是否已存在当前评论
    def queryByRpid(self, rpid):
        sql = "select id from answer where rpid='" + str(rpid) + "'"
        rw = self.dbHelper.queryOne(sql)
        return rw




