#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开

def is_odd(n):
    return n % 2 == 1

#L = list(filter(is_odd, range(1, 20)))

L = list(filter(lambda x: x % 2 == 1,range(1,20)))

print(L)

