#-*- coding: utf-8 -*-
from BzProject.spiders.com.bz.LogManager import LogManager
from BzProject.spiders.com.bz.DbHelpers import DbHelpers

#读取分页数据
class JsonUtils(object):
    log=LogManager()
    helper=DbHelpers()

    #存放评论下的讨论内容
    nextArr=[]

    answerArr=[]

    def readNextPage(self,data):
        arr=[]
        dict={}
        for obj in data:
            param = []
            aid=obj['aid']#int
            arcrank=obj['arcrank']#str
            arcurl=obj['arcurl']#str
            author=obj['author']#str
            badgepay=obj['badgepay']#str
            description=obj['description']#str
            duration=obj['duration']#str
            favorites=obj['favorites']#int
            id=obj['id']#int id=aid
            is_pay=obj['is_pay']#int
            mid=obj['mid']#int 作者id
            pic=obj['pic']#str
            play=obj['play']#int
            pubdate=obj['pubdate']#int
            rank_index=obj['rank_index']#int
            rank_offset=obj['rank_offset']#int
            rank_score=obj['rank_score']#int
            review=obj['review']#int
            senddate=obj['senddate']#int
            tag=obj['tag']#str
            title=obj['title']#str
            type=obj['type']#str
            typeid=obj['typeid']#str
            typename=obj['typename']#str
            video_review=obj['video_review']
            # print("上传人："+author+"描述："+description+"连接地址："+arcurl+"av编号："+str(id))
            dict.__setitem__(id,arcurl)
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

        self.addData(arr)
        return dict

    #读取总页数
    def getPageCount(data):
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

        print("总页数" + str(acount) + "count：" + str(pageCount) + "一页多少：" + str(pageSize) + " 当前页码：" + str(
            pageNum) + "总页码" + str(pageAcount))
        return pageAcount
    #读取评论
    def getComments(self,data):

        #读取内容前清空数组
        del self.answerArr[:]
        del self.nextArr[:]
        self.commonMethod(data)#对数组进行添加数据
        if self.answerArr is not None:
            sql="insert into answer(rpid,answercount,ctime,floor,answerike,mid,oid,parent," \
                "rcount,device,message,displayRank,avatar,current_level,uname,rank,sex,sign)" \
                "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.helper.executeSqlMany(sql, self.answerArr)

        else:
            print("数组为空，不执行新增")

        return self.nextArr
    #公共读取方法
    def commonMethod(self,data):

        for obj in data:
            replies = obj['replies']
            params=self.readDataDetails(obj)
            if params is not None:#判断读取到的评论是否为空 或者已经读取过
                ln=len(params)
                if ln!=0:
                    self.answerArr.append(params)


            if replies is None:
                print("当前repliesw为空  不执行写入txt操作")
            else:
                print("replies不为空")
                j=len(replies)
                print("回复数量："+str(j))
                self.commonMethod(replies)

    #读取评论
    def readDataDetails(self,obj):
        #添加list批量新增的字段
        params=[]
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
        rw=self.queryByRpid(rpid)
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


        logTxt="姓名：" + uname + " rpid：" + str(rpid) + " 回复内容：" + message+"\n"
        self.writeLog(logTxt)
        #默认评论下讨论只显示前3条
        if rcount>3:
            print("rowcoutn  是否大于3")
            self.readReplyNext(rcount, oid, rpid)
        return params


    # 读取评论下的相互评论
    def readReplyNext(self, rcount, oid, rpid):
        # 读取b站 互相回复

        if rcount > 3:
            pnu = rcount / 10 # 正常除法
            pnum = rcount // 10  # 取整数部分
            pg = 1
            print("pnu: " + str(pnu) + " pnum :" + str(pnum))
            if pnu > pnum:
                if pnu < 1:
                    pnum = 1
                pg = pnum + 1
            else:
                pg = pg + 1

            # print("计算完毕后的pg：" + str(pg))
            for i in range(1, pg):
                tarRepliesURL = "https://api.bilibili.com/x/v2/reply/reply?pn=1&type=1&oid=" + str(oid) + "&ps=10&root=" + str(rpid) + ""

                self.nextArr.append(tarRepliesURL)

        if len(self.nextArr) == 0:
            print("评论下的相互回复为空，不执行再次读取")
        else:
            print("评论下的相互回复为不为空，执行再次读取")


    def writeLog(self,logtxt):
        f = open(r'E:\Pythonwork\BzProject\log\log.txt', 'a+', encoding='utf-8')
        f.write(logtxt)
        f.close()

    #批量新增
    def addData(self,param):
        # print("=========新增至数据库===========")
        if param is not None:
            sql="insert into video (aid,arcrank,arcurl,author,badgepay,description,duration,favorites," \
                "sid,is_pay,mid,pic,play,pubdate,rank_index,rank_offset,rank_score,review,senddate,tag,title,tpe,typeid,typename,video_review)values(%s,%s,%s," \
                "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.helper.executeSqlMany(sql,param)

    #查询是否已存在当前评论
    def queryByRpid(self,rpid):
        sql = "select id from answer where rpid='" + str(rpid) + "'"
        rw=self.helper.queryOne(sql)
        return rw




if __name__=="__main__":

    LogManager.writeLog(JsonUtils.log, "HHAHH")







