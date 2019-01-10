# coding = utf-8
from Crypto.Cipher import AES
import base64
import requests
import json

headers = {
    'Cookie': '_iuqxldmzr_=32; _ntes_nnid=f6d6f2b93a7a86d66d5089867f22a216,1546483116021; _ntes_nuid=f6d6f2b93a7a86d66d5089867f22a216; WM_TID=d7Rx0MyscLhEFBUQEQd4hBMCxg3OUPLE; Province=0590; City=0793; UM_distinctid=16812f8af355-0a5ce8589fef42-58422116-1fa400-16812f8af36c94; vjuids=86bf1431.16812f8daac.0.3f94a85de485; vjlast=1546506525.1546506525.30; __gads=ID=ec02424a1178b974:T=1546506466:S=ALNI_MbETf8hLGpEOaU6NFVePumfYQqy0A; vinfo_n_f_l_n3=884225362055b286.1.0.1546506525409.0.1546506543680; JSESSIONID-WYYY=Uh9fzOoITNp4ub6Y3Tufss1qwMRpKa1TpRk3%2BaPcO3NPUOEZ%2FxkGSEi1683%2BjDZmNEOJp9hIlC0Yg3Ypbc9HE7SZMaOjWxCIsf%5Cd4U6nX7jP%5CU%5C5d1rkDE47bsZPKz639gR6QulHSOehTGF3AdETPJQsBwP%2BI4NXbhfFlx7XA%5CvlrjDU%3A1546825050089; __utma=94650624.1693375539.1546483117.1546590243.1546823250.9; __utmc=94650624; __utmz=94650624.1546823250.9.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=20EurL4SPsfx9DQSm0BS67LUeBfwkhdEsA2nULkNWWbMXrJxJ1GKh48WKpK%2BAcDqv%2FDGe91OdqfG7aNUXmHJvXx5T32SrMD0F1bM%2FNJwU%2FW6xDrHU8aqYcNfcegtLmcnenk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccb2798cb500d3ec418eeb8fb3d54f929f9bbaee6886b8a290bc509a959c94d72af0fea7c3b92af2f08b96f148f88da094e574fb9c9fb4f03c828dfad8cf5fa79eaa98ea64a89bbda2b1669794a5afd65da2939893c9748aef89aceb40fc898591ca2183bd8c92f5258899abdab445a8afaaa8b66b8e8b988ecb42b688b8d6d739f28dbeaec73c86efaeaeae468aa99bd0d63ebc9cbea9d834a3af9784cd6ea1bba995cf67a1b2ab8fea37e2a3; __utmb=94650624.5.10.1546823250',
    'Referer': 'http://music.163.com/',
    'Accept-Language':"zh-CN,zh;q=0.9",
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

}
first_param = "{rid:\"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"
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


def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    # encrypt_text = base64.b64encode(encrypt_text)
    encrypt_text = str(base64.b64encode(encrypt_text))[2:-1]
    return encrypt_text


def get_json(url, params, encSecKey):
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data)
    return response.content


if __name__ == "__main__":
    url = "http://music.163.com/weapi/v1/resource/comments/A_PL_0_2522547939?csrf_token="
    params = get_params();
    encSecKey = get_encSecKey();
    json_text = get_json(url, params, encSecKey)
    j_text=str(json_text, encoding="utf8")
    json_dict = json.loads(j_text)
    print(json_dict['total'])
    for item in json_dict['comments']:

        print(item)
        #