# -*- coding:utf-8 -*-
import urllib
import urllib2
import re



user_agent = 'Mozilla/5.0 (Windows NT 6.1)'
headers = { 'User-Agent' : user_agent }
#网页循环
for page in range (1,71):    
    url = 'http://www.haha365.com/ymgs/index_'+str(page)+'.htm'

    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason 
    content_pattern = re.compile('<div class="cat_llb">.*?<A href=".*?">(.*?)</a>', re.S)
    content_pattern1 = re.compile('<div class="cat_llb">.*?<p>(.*?)</p>', re.S)
    
    content_list = re.findall(content_pattern, html)
    content_list1 = re.findall(content_pattern1, html)
#标题和内容更迭输出
    for item1 in content_list1:
        for item in content_list:
            print item
            del content_list[0]
            print '\n'
            break
        print item1
        print '\n'
#输入“回车”显示下一页，“Q”退出        
    input = raw_input()    
    if input == "Q":       
        break


    


    
