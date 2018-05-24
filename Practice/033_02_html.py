#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开

#找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

from html.parser import HTMLParser
from urllib import request
import re
import ssl

class MyHTMLParser(HTMLParser):
    flag = 0
    res = []
    is_get_data = 0

    def handle_starttag(self, tag, attrs):
        # 首先找到包裹事件的元素
        if tag == 'ul':
            for attr in attrs:
                if re.match(r'list-recent-events', attr[1]):
                    # print(type(attr))   #<class 'tuple'>
                    # print('attr:',attr) #attr: ('class', 'list-recent-events menu')
                    self.flag = 1

        # 处理包裹事件名称的a元素
        if tag == 'a' and self.flag == 1:
            self.is_get_data = 'title'

        # 处理时间的time元素
        if tag == 'time' and self.flag == 1:
            self.is_get_data = 'time'

        # 处理包裹地点的time元素
        if tag == 'span' and self.flag == 1:
            self.is_get_data = 'addr'

    def handle_endtag(self, tag):
        if self.flag == 1 and tag == 'ul':
            self.flag = 0

    def handle_data(self, data):
        if self.is_get_data and self.flag == 1:
            if self.is_get_data == 'title':
                self.res.append({self.is_get_data: data})
            else:
                self.res[len(self.res) - 1][self.is_get_data] = data
            self.is_get_data = None


parser = MyHTMLParser()

with request.urlopen('https://www.python.org/events/python-events/',context = ssl._create_unverified_context()) as f:
    data = f.read().decode('utf-8')

parser.feed(data)
for item in parser.res:
    print('---------------')
    for k,v in item.items():
        print("%s : %s" % (k,v))