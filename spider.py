# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib

 -*- coding:utf-8 -*-
__author__ = 'Liubai'

"""
抓取网页可以使用库urllib, urllib2,但鉴于你调用十分麻烦，所以我们第三方的reuqests包，
一个API十分友好的包，如果你没有安装请自行按照下面命令安装：
pip install requests
"""

"""
希望做一个这样的爬虫类：
支持登陆
支持cookies
支持Proxy
支持多线程
支撑压缩传输
"""

import requests
import time

proxy ={'http': 'http://109.120.22.4:8080'}
class spider(object):
    def __init__(self, url, headers, data, proxy, threads):
        self.headers = {
            #伪装成浏览器访问
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157',
            #反盗链
            'Referer': url,
            #文件以压缩格式传输
            'Accept-Encoding': 'gzip, deflate'
        }
        self.headers.update(headers)
        self.proxy = proxy
        self.data = data
        self.threads = threads

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1)'
    }
    data = {
        'username': 'Liubai',
        'password': 'XXXXXX'
    }
    post_data = urllib.urlencode(data)
    proxy_handler = urllib2.ProxyHandler({'http': 'http://109.120.22.4:8080'})
    cookie = cookielib.CookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(proxy_handler, cookie_handler)
    #response = opener.open(url,post_data,headers=headers)
    request = urllib2.Request(url)
    response = opener.open(request)
    return response
    #return response.read()

if __name__ == '__main__':
    resp = get_page('http://www.baidu.com')
