#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开

import chardet

print(chardet.detect(b'Hello, world!'))

# data = '离离原上草，一岁一枯荣'.encode('gbk')
# data = '离离原上草，一岁一枯荣'.encode('utf-8')
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))