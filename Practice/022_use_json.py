#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开


import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)