# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from selenium.webdriver.common.keys import Keys
import json
from selenium.webdriver.common.action_chains import ActionChains

#Selenium读取qq空间
class QzoneClient(object):

    def __init__(self):
        options = webdriver.ChromeOptions()
        # 设置无图模式
        prefs = {
            'profile.default_content_setting_values': {
                'images': 2
            }
        }
        options.add_argument('--headless')  # 浏览器隐藏
        options.add_argument('--disable-gpu')
        options.add_experimental_option('prefs', prefs)  # 设置无图模式
        # browser = webdriver.Chrome(chrome_options=options)
        self.browser = webdriver.Chrome()

        self.wait = WebDriverWait(self.browser, 5)
        print("初始化")

    def startQQZone(self):
        try:
            # qq空间地址
            tarURL = 'https://user.qzone.qq.com'
            self.browser.get(tarURL)
            try:
                self.browser.find_element(By.NAME, 'login_frame')  # 发现登录的frame

            except:
                raise
            else:
                try:
                    self. browser.switch_to_frame('login_frame')  # 发现login_frame 进入
                    login = self.wait.until(EC.element_to_be_clickable((By.ID, 'img_out_625201089')))  # 获取点击按钮 也可以进行输入账号密码
                    login.click()
                except Exception as e:
                    raise
                time.sleep(2)

                # 读取新地址
                newURL = "https://user.qzone.qq.com/{}".format("625201089")
                self.browser.get(newURL)
                #个人中心  读取自己个人中心qq好友发的说说
                mycenter = self.browser.find_element_by_id("aIcenter")
                time.sleep(3)
                centerURL = mycenter.get_attribute("href")

                # 读取个人中心
                self.browser.get(centerURL)
                time.sleep(3)
                html = self.browser.page_source
                # soup = BeautifulSoup(html, "html.parser")
                doc = pq(html)
                liTags = doc('#feed_friend_list >li').items()
                self.readRepliesData(liTags)
                # 读取下拉刷新的数据
                arr = []
                self.readRefreshData(arr)
        except Exception as e:
            print(e)

    # 读取下拉刷新数据 进行递归读取  每次都触发下拉事件
    def readRefreshData(self,arr):
        for i in range(10):
            # 滚动条操作
            TargetElement = self.browser.find_element_by_id("feed_friend_tips")  # 鼠标移动到某个元素
            ActionChains(self.browser).move_to_element(TargetElement).perform()
            ActionChains(self.browser).move_to_element(TargetElement).perform()
            # ActionChains(browser).move_to_element(TargetElement).perform()
            # ActionChains(browser).move_to_element(TargetElement).perform()

            time.sleep(120)
            print("拖动滑动条到底部...")
            htmlRefresh = self.browser.page_source
            dc = pq(htmlRefresh)
            refreshUlItems = dc('li[class="feed_page_container"]').children().items()
            for ulElement in refreshUlItems:

                dataPage = ulElement.attr("data-page")
                if dataPage in arr:
                    print("已经读取过，不允许重复读取" + str(dataPage))
                else:
                    arr.append(dataPage)
                    print("==============读取下拉后的数据================")
                    liElements = ulElement.find('li[class="f-single f-s-s"]').items()
                    self.readRepliesData(liElements)
                print("页数" + str(dataPage))

    # 读取li内的信息
    def readRepliesData(self,liItems):
        for item in liItems:
            # 用户发说说时间
            uName = item.find('div[class="f-nick"] a').text()  # 用户名
            createDate = item.find('div[class="info-detail"] span').text()  # 发表事件
            uSign = item.find('div[class="info-detail"] a').text()  # 用户签名
            # 说说内容
            f_info = item.find('div[class="f-info"]').text()  # 说说内容
            # 是否有上传图片
            fctItems = item.find('div[class="qz_summary wupfeed"] div')
            picItems = fctItems.find('img').items()
            self.readPicItems(picItems, uName)  # 读取图片

            freprint = item.find('div[class="f-reprint"] span').text()  # 手机  pc或其他
            # 回复
            viewCount = item.find('div[class="f-op-detail f-detail content-line"] a').text()  # 浏览次数
            likeCount = item.find('div[class="user-list"] span').text()  # 赞人数
            aItems = item.find('div[class="user-list"] a').items()  # 赞的人
            likeArr = []
            for aitem in aItems:
                likeUser = aitem.text()
                likeArr.append(likeUser)
            likeStr = ",".join(str(i) for i in likeArr)

            # 读取回复的li
            repliesLiItems = item.find('div[class="mod-comments"] div ul li').items()
            self.readCommonsReplies(repliesLiItems)

            print(
                "用户：" + uName + "\t创建时间：" + createDate + "\t说说内容：" + f_info + "\t浏览数量：" + freprint + "\t浏览数量：" + viewCount + "\t赞人数：" + likeCount + "\t赞的人：" + likeStr)

    # 读取说说下的评论li
    def readCommonsReplies(self,liItems):
        for liItem in liItems:
            dataUin = liItem.attr("data-uin")
            dataNick = liItem.attr("data-nick")
            singleReplyItem = liItem.find('div[class="single-reply"]')
            commentsContent = singleReplyItem.find('div[class="comments-content"]')
            repliesTxt = commentsContent.find('a').text()  # 回复内容
            repliesDetail = commentsContent.text()  # 具体内容
            repliesTime = commentsContent.find('div[class="comments-op"] span').text()
            # 读取回复
            modCommentsSub = liItem.find('div[class="comments-list mod-comments-sub"] ul');
            modCommentsSubLis = modCommentsSub.find("li").items()
            self.readCommonsReplies(modCommentsSubLis)
            print(
                "用户账号：" + dataUin + "\t用户昵称：" + dataNick + "\t回复内容：" + repliesTxt + "具体内容：" + repliesDetail + "\t回复时间：" + repliesTime)

    # 读取图片
    def readPicItems(self,picItems, uname):
        for picItem in picItems:
            picURL = picItem.attr("src")
            print("当前用户名：" + uname + "图片地址：" + picURL)





