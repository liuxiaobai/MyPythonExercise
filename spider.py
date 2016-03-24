# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib

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
