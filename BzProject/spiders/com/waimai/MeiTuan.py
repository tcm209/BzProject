# -*- coding: utf-8 -*-
import requests
import json
from scrapy.selector import Selector

class MeiTuan(object):

    def __init__(self):
        self.baseurl=""
        pass


    def getDatas(self):
        # wd=搜索地址
        # ak=
        # c=厦门市uid
        # rn=一页显示多少行数据
        # 根据搜索汉字  获取地址列表https://api.map.baidu.com/?qt=s&c=194&wd=厦门市集美区嘉庚体育馆&rn=5&ie=utf-8&oue=1&fromproduct=jsapi&res=api&ak=Tg7cjyoPXqqliG19hIohzDWK
        pass

    # 获取商家列表header
    def getResterrauntHeader(self):
        header={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': '__mta=256728372.1551081732900.1551150035965.1551150180208.5; _lxsdk_cuid=1692357825ac8-044abe7fadb35-3d644701-1fa400-1692357825a51; w_utmz="utm_campaign=(direct)&utm_source=(direct)&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_uuid=qJ6kdgiWK546bKrwoTIzLPqeGsSawLENhTGD0oSJAxzRlZ-P-hmr4CIyvDDNEGVy; _ga=GA1.3.922421511.1551076161; _gid=GA1.3.1115061729.1551076161; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mtcdn=K; waddrname="%E5%98%89%E5%BA%9A%E4%BD%93%E8%82%B2%E9%A6%86-%E8%B4%B5%E5%AE%BE%E5%87%BA%E5%85%A5%E5%8F%A3"; w_geoid=ws7gztpc5y2x; w_cid=350211; w_cpy=jimeiqu; w_cpy_cn="%E9%9B%86%E7%BE%8E%E5%8C%BA"; w_ah="24.593101870268583,118.11383195221424,%E5%98%89%E5%BA%9A%E4%BD%93%E8%82%B2%E9%A6%86-%E8%B4%B5%E5%AE%BE%E5%87%BA%E5%85%A5%E5%8F%A3"; w_visitid=7d59c5d6-a4a7-4b0d-8504-34b6c27b46f1; _lxsdk=1692357825ac8-044abe7fadb35-3d644701-1fa400-1692357825a51; JSESSIONID=j5s6hnl6rsr81wzolfpejierz; _gat=1; _lxsdk_s=16927bc5128-501-360-758%7C%7C11',
            'Host': 'waimai.meituan.com',
            'Pragma': 'no-cache',
            'Referer': 'http://waimai.meituan.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        }
        return header

    # 展示所有的商家http://waimai.meituan.com/home/ws7gztpc5y2x
    def resterauntList(self):
        response=requests.get(url="http://waimai.meituan.com/home/ws7gztpc5y2x",headers=self.getResterrauntHeader())
        self.responseResteraunt(response)


        pass
    # 获取列表html
    def responseResteraunt(self,response):
        contentData=Selector(text=response.content)

        items=contentData.xpath("//div[@class='rest-list']//ul//li")
        for item in items:
            lennum=len(item.xpath("div//div[@class='restaurant']"))
            if lennum!=0:
                data_title = item.xpath("div//div[@class='restaurant']//@data-title")[0].extract()
                data_poiid = item.xpath("div//div[@class='restaurant']//@data-poiid")[0].extract()
                href = item.xpath("div//div[@class='restaurant']//a[@class='rest-atag']//@href")[0].extract()  # 店内详细内容
                score_num = item.xpath("div//div[@class='restaurant']//a[@class='rest-atag']//span[@class='score-num fl']")[0].extract()  # 评分
                print("店名：" + data_title.encode("gbk","ignore").decode("gbk","ignore") + "\t评分：" + score_num + "\t地址：" + href)
                self.getPjDatas(data_poiid,1)
    # 加载更多
    # token  目前还没找到还原方法
    def loadingList(self):
        formdata={
            "classify_type":"cate_all",
            "sort_type": "0",
            "price_type": "0",
            "support_online_pay": "0",
            "support_invoice": "0",
            "support_logistic": "0",
            "page_offset": "0",
            "page_size": "20",
            "mtsi_font_css_version": "20ad699b",
            "uuid": "qJ6kdgiWK546bKrwoTIzLPqeGsSawLENhTGD0oSJAxzRlZ-P-hmr4CIyvDDNEGVy",
            "platform": "1",
            "partner": "4",
            "originUrl": "http//waimai.meituan.com?home&ws7gztpc5y2x"
        }
        response=requests.post(url="http://waimai.meituan.com/ajax/poilist?_token",headers=self.loadingListHeader(),data=formdata)
        self.loadingDatas(response)

        pass

    def loadingDatas(self,reponse):
        content=reponse.content
        print(content)
        pass

    # 获取列表
    def loadingListHeader(self):
        header={
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '329',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '_lxsdk_cuid=1692357825ac8-044abe7fadb35-3d644701-1fa400-1692357825a51; w_utmz="utm_campaign=(direct)&utm_source=(direct)&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_uuid=qJ6kdgiWK546bKrwoTIzLPqeGsSawLENhTGD0oSJAxzRlZ-P-hmr4CIyvDDNEGVy; _ga=GA1.3.922421511.1551076161; _gid=GA1.3.1115061729.1551076161; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mtcdn=K; waddrname="%E5%98%89%E5%BA%9A%E4%BD%93%E8%82%B2%E9%A6%86-%E8%B4%B5%E5%AE%BE%E5%87%BA%E5%85%A5%E5%8F%A3"; w_geoid=ws7gztpc5y2x; w_cid=350211; w_cpy=jimeiqu; w_cpy_cn="%E9%9B%86%E7%BE%8E%E5%8C%BA"; w_ah="24.593101870268583,118.11383195221424,%E5%98%89%E5%BA%9A%E4%BD%93%E8%82%B2%E9%A6%86-%E8%B4%B5%E5%AE%BE%E5%87%BA%E5%85%A5%E5%8F%A3"; _lxsdk=1692357825ac8-044abe7fadb35-3d644701-1fa400-1692357825a51; wm_order_channel=default; openh5_uuid=; uuid=; w_visitid=c2c073bf-341c-4165-b41d-2db0b4290572; JSESSIONID=rokjqpcgnvglztbzhlk2eod2; _lxsdk_s=169287e222f-17c-116-7fb%7C%7C1',
            'Host': 'waimai.meituan.com',
            'Origin': 'http://waimai.meituan.com',
            'Pragma': 'no-cache',
            'Referer': 'http://waimai.meituan.com/home/ws7gztpc5y2x',
            'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
            'X-FOR-WITH': '4nuzmoPekORht9mipXMbKXp9uNccoaQk4RgM2PnEucAYeNM8nHnndeqV0My4946hf8Afx4nNuzUT5PTZjNHv2gySmMPs2r9mvqjImUKlbmMdMvcSCWB+hbkHW+SJMh5dVz7HGoomrdRSRLW3zSF6QQ==',
            'X-Requested-With': 'XMLHttpRequest'
        }
        return header



    # 获取读取评价信息的header
    def getPjHeader(self):
        header={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "240",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": '_lxsdk_cuid=1692357825ac8-044abe7fadb35-3d644701-1fa400-1692357825a51; w_utmz="utm_campaign=(direct)&utm_source=(direct)&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_uuid=qJ6kdgiWK546bKrwoTIzLPqeGsSawLENhTGD0oSJAxzRlZ-P-hmr4CIyvDDNEGVy; _ga=GA1.3.922421511.1551076161; _gid=GA1.3.1115061729.1551076161; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mtcdn=K; waddrname="%E5%98%89%E5%BA%9A%E4%BD%93%E8%82%B2%E9%A6%86-%E8%B4%B5%E5%AE%BE%E5%87%BA%E5%85%A5%E5%8F%A3"; w_geoid=ws7gztpc5y2x; w_cid=350211; w_cpy=jimeiqu; w_cpy_cn="%E9%9B%86%E7%BE%8E%E5%8C%BA"; w_ah="24.593101870268583,118.11383195221424,%E5%98%89%E5%BA%9A%E4%BD%93%E8%82%B2%E9%A6%86-%E8%B4%B5%E5%AE%BE%E5%87%BA%E5%85%A5%E5%8F%A3"; w_visitid=7d59c5d6-a4a7-4b0d-8504-34b6c27b46f1; _lxsdk=1692357825ac8-044abe7fadb35-3d644701-1fa400-1692357825a51; wm_order_channel=default; openh5_uuid=; uuid=; _lxsdk_s=16927bc5128-501-360-758%7C%7C27; JSESSIONID=18wn96ae6ssyq1fm0ef2iuxr4; _gat=1',
            "Host": "waimai.meituan.com",
            "Origin": "http://waimai.meituan.com",
            "Pragma": "no-cache",
            "Referer": "http://waimai.meituan.com/comment/144803440980910720",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",

        }
        return header



    # 读取评价内容
    def getPjDatas(self,wmpoiIdStr,pagenum):
        # 评价地址http://waimai.meituan.com/ajax/comment
        # 参数 144803440980910720
        # offset是页数
        formdata={
            "wmpoiIdStr":wmpoiIdStr,
            "offset":pagenum,
            "has_content":1,
            "score_grade":1,
            "uuid":"",
            "platform":1,
            "partner":4,
            "originUrl":"http//waimai.meituan.com&comment&"+wmpoiIdStr
        }
        response=requests.post("http://waimai.meituan.com/ajax/comment",headers=self.getPjHeader(),data=formdata)
        self.responsePj(response)

        pass

    # 评价详细
    def responsePj(self,respose):
        contentData=respose.content
        contentText=str(contentData,encoding="utf-8")
        jsondata=json.loads(contentText)
        msg=jsondata["msg"]
        code=jsondata["code"]
        page_total=jsondata["data"]["page_total"]
        wmCommentVos=jsondata['data']['wmCommentVo']
        for vo in wmCommentVos:
            username=vo['wmComment']['username']
            wmComment=vo['wmComment']['clean_comment']
            print("用户："+username.encode("gbk","ignore").decode("gbk","ignore")+"\t评价内容："+wmComment.encode("gbk","ignore").decode("gbk","ignore"))



if __name__=="__main__":
    mt=MeiTuan()
    mt.loadingList()





