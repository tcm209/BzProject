# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
import requests
import json
from binascii import b2a_hex, a2b_hex

headers = {
    'Cookie': '_iuqxldmzr_=32; _ntes_nnid=f6d6f2b93a7a86d66d5089867f22a216,1546483116021; _ntes_nuid=f6d6f2b93a7a86d66d5089867f22a216; WM_TID=d7Rx0MyscLhEFBUQEQd4hBMCxg3OUPLE; Province=0590; City=0793; UM_distinctid=16812f8af355-0a5ce8589fef42-58422116-1fa400-16812f8af36c94; vjuids=86bf1431.16812f8daac.0.3f94a85de485; vjlast=1546506525.1546506525.30; __gads=ID=ec02424a1178b974:T=1546506466:S=ALNI_MbETf8hLGpEOaU6NFVePumfYQqy0A; vinfo_n_f_l_n3=884225362055b286.1.0.1546506525409.0.1546506543680; JSESSIONID-WYYY=Uh9fzOoITNp4ub6Y3Tufss1qwMRpKa1TpRk3%2BaPcO3NPUOEZ%2FxkGSEi1683%2BjDZmNEOJp9hIlC0Yg3Ypbc9HE7SZMaOjWxCIsf%5Cd4U6nX7jP%5CU%5C5d1rkDE47bsZPKz639gR6QulHSOehTGF3AdETPJQsBwP%2BI4NXbhfFlx7XA%5CvlrjDU%3A1546825050089; __utma=94650624.1693375539.1546483117.1546590243.1546823250.9; __utmc=94650624; __utmz=94650624.1546823250.9.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=20EurL4SPsfx9DQSm0BS67LUeBfwkhdEsA2nULkNWWbMXrJxJ1GKh48WKpK%2BAcDqv%2FDGe91OdqfG7aNUXmHJvXx5T32SrMD0F1bM%2FNJwU%2FW6xDrHU8aqYcNfcegtLmcnenk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccb2798cb500d3ec418eeb8fb3d54f929f9bbaee6886b8a290bc509a959c94d72af0fea7c3b92af2f08b96f148f88da094e574fb9c9fb4f03c828dfad8cf5fa79eaa98ea64a89bbda2b1669794a5afd65da2939893c9748aef89aceb40fc898591ca2183bd8c92f5258899abdab445a8afaaa8b66b8e8b988ecb42b688b8d6d739f28dbeaec73c86efaeaeae468aa99bd0d63ebc9cbea9d834a3af9784cd6ea1bba995cf67a1b2ab8fea37e2a3; __utmb=94650624.5.10.1546823250',
    'Referer': 'http://music.163.com/',
    'Accept-Language':"zh-CN,zh;q=0.9",
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

}
st=   '\\'+"s-fc7"+'\\'+""

print(st)
# {"id":"26326159","lv":-1,"tv":-1,"csrf_token":""}
f="{\"hlpretag\":\"<span class=\"s-fc7\">\",\"hlposttag\":\"</span>\",\"s\":\"知否\",\"type\":\"1\",\"offset\":\"0\",\"total\":\"true\",\"limit\":\"30\",\"csrf_token\":\"\"}"
# "{"hlpretag":"<span class=\"s-fc7\">","hlposttag":"</span>","s":"知否","type":"1","offset":"0","total":"true","limit":"30","csrf_token":""}"
first_param='{hlpretag:"<span class=\"s-fc7\">",hlposttag:"</span>",s:"Wait For You",type:"1",offset:"0",total:"true",limit:"30",csrf_token:""}'
    # "{hlpretag:\"<span class=\"s-fc7\">\",hlposttag:\"</span>\",s:\"知\",type:\"1\",offset:\"0\",total:\"true\",limit:\"30\",csrf_token:\"\"}"
# first_param="{id:\"26326159\", lv:\"-1\", tv:\"-1\", csrf_token:\"\"}"
# first_param="{rid:\"\", offset:\"100\", total:\"false\", limit:\"20\", csrf_token:\"\"}"
second_param = "010001"
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud"


def get_params():
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)

    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey

'{hlpretag:\"<span class=\"s-fc7\">\",hlposttag:\"</span>\",s:"知",type:"1",offset:"0",total:"true",limit:"30",csrf_token:""}'
def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    print(len(text))
    encrypt_text = encryptor.encrypt(text)#text存在汉字时出现异常  待解决
    # encrypt_text = base64.b64encode(encrypt_text)
    encrypt_text = str(base64.b64encode(encrypt_text))[2:-1]
    return encrypt_text

def AES_encrypt_Other(text, key, iv):
    aes=AES.new(add_to_16(key),AES.MODE_CBC,iv)
    encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf-8').replace('\n', '')
    return encrypted_text

def add_to_16(value):
    while len(value)%16 !=0:
        value+='\0'
    return str.encode(value)



def get_json(url, params, encSecKey):
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data)
    return response.content
 #解析评论response
def answerAPL(json_text):
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
    for item in comments:
        content = item['content']  # 内容
        print("评论："+content.encode("gbk", 'ignore').decode("gbk", "ignore"))



if __name__ == "__main__":
    # url = "https://music.163.com/weapi/v1/resource/comments/A_PL_0_924680166?csrf_token="
    # params = get_params()
    # # url="https://music.163.com/weapi/song/lyric?csrf_token="
    # encSecKey = get_encSecKey()
    # json_text = get_json(url, params, encSecKey)
    # answerAPL(json_text)
    # # print(json_dict['lrc']['lyric'])

    url="https://music.163.com/weapi/cloudsearch/get/web?csrf_token=982bc4b2d94d53539c85a84705cc4405"
    p1=get_params()
    # p="1dxfQyCWDJnkCimkT26raJDEIiUFefMQvuaAywN/7QT/JhOKt4tSkRC717zUb0Glmb8Fbxl5ieo/KvIWcNs2w8OCiI7MpGPWmRtL3c+WlO2eONbgJ66NaH1eGVdNuBhocL6TAyOzP5k84tRbiD7fkDWBh13s5l6RPWJQvltUOX85ZSO2V6VwGbat4QpK2bPHjy0yee8kEHQ18Di+Jlfdt4c7Y7yPkRF8CyS9LzRO6ldotUxZ1LIUchQQA431XlvyG1/K3/+66lU4SXiSBGUc27Q1RpG8of0pRMb0XB1IZth1AeXhlixXlatv5/dNj+98NJyoNT4wQ9lF0oLDnCM6sWlTS0SoqhwE6GE0f7rK0eloUpxhhT668nyGzki66GPa"
    # p="TomqMOcXXj4lfrQdDyXN/FJHelORunrDUKut7tK99U0P8EkSU+6tc411DtqZ2zSL4YgoMWrD0VF3E7o8JSzeMR40QAplI/bljOYI/EEjZNFrSWbMcxdqe53gIi7guCCh/G4Pt1hbVxKQKdnHzA/ko3u8WNcoyouonh5tT1lnSyK2P3HScBqRuysYZpMwLqGDYeaOV18L38IYXxkyVYj4R7j533QwLxNPraaBmnfo41y1oIZZ4XKyYbHhkvkDMiucViuP/Wvm/k8E4I+lPolRiw=="
    e="6d9bbd9a999d69005e68a853d386c4531a70bdbb1c03a200d0c5b4b59194a0237e9de8d2c943b236af9bcae581b8eb3ddf01a1ec7bb4cfc9b592aef6611da19ddd727305d8118ecf4834a7a192ede6e727b4a642a080f25702d56cbf43fd224b6c75acb739cab96cd2c220206cc0b90ce0cb3f7685718af9a84ce1c8879d7229"

    json_text = get_json(url, p1, e)
    j_text = str(json_text, encoding="utf8")
    json_dict = json.loads(j_text)
    print(json_text)


#         #
# 13位时间转换
# import time
#
# timestrap=float(1547163644951/1000)
# time_local=time.localtime(timestrap)
# dt=time.strftime("%Y-%m-%d %H:%M:%S",time_local)
# print(dt)