#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开

#请将本地一个文本文件读为一个str并打印出来：
fpath = r'/Users/tianzeng/Desktop/READ_ME2.txt'

with open(fpath,'r') as f:
    s = f.read()
    print(s)





