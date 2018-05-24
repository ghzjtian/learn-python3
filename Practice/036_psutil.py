#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开


import psutil


print( psutil.cpu_count() )# CPU逻辑数量

print(psutil.cpu_count(logical=False)) # CPU物理核心

# 2说明是双核超线程, 4则是4核非超线程


print(psutil.virtual_memory())