import requests
from random import random
from subprocess import check_output

def format_s(s):
    return {
        item.split(':', 1)[0].strip(): item.split(':', 1)[1].strip() for item in s.split('\n') if item
    }


def createGuid():
    return hex(int((1 + random()) * 0x10000))[3:]


def Guid():
    return createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid()

def result(vjkl5):
    return check_output(['node','./result.js',vjkl5]).decode('utf8').strip()

# session = requests.Session()
# List
url = 'http://wenshu.court.gov.cn/List/List'
params = """sorttype:1
conditions:searchWord 1 AJLX  案件类型:刑事案件"""
headers = """Host:wenshu.court.gov.cn
Origin:http://wenshu.court.gov.cn
Referer:'http://wenshu.court.gov.cn/'
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36
X-Requested-With:XMLHttpRequest"""

vjkl5 = requests.get(url=url, params=format_s(params), headers=format_s(headers)).cookies.get('vjkl5')

#GetCode
url = 'http://wenshu.court.gov.cn/ValiCode/GetCode'
guid = Guid()
data = {
    'guid': guid
}
headers = """Content-Type:application/x-www-form-urlencoded; charset=UTF-8
Cookie:vjkl5={vjkl5:s}
Host:wenshu.court.gov.cn
Origin:http://wenshu.court.gov.cn
Referer:http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36
X-Requested-With:XMLHttpRequest""".format(vjkl5=vjkl5)
number = requests.post(url=url, data=data, headers=format_s(headers)).text

#ListContent
url = 'http://wenshu.court.gov.cn/List/ListContent'
vl5x = result(vjkl5)
data = {
    'Param': '案件类型:刑事案件',
    'Index': '1',
    'Page': '5',
    'Order': '法院层级',
    'Direction': 'asc',
    'vl5x': vl5x,
    'number': number,
    'guid': guid
}
headers = """Accept:*/*
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Connection:keep-alive
Content-Length:240
Content-Type:application/x-www-form-urlencoded; charset=UTF-8
Cookie:Hm_lvt_3f1a54c5a86d62407544d433f6418ef5=1511404343,1511496554,1511508707,1511512439; Hm_lpvt_3f1a54c5a86d62407544d433f6418ef5=1511513570; vjkl5={vjkl5:s}; _gscu_2116842793=107348165nru1x93; _gscs_2116842793=t11516304r5xxer18|pv:1; _gscbrs_2116842793=1
Host:wenshu.court.gov.cn
Origin:http://wenshu.court.gov.cn
Referer:http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36
X-Requested-With:XMLHttpRequest""".format(vjkl5=vjkl5)

content = requests.post(url=url, data=data, headers=format_s(headers))
print(content.text)