#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#请用sorted()对上述列表分别按名字排序：

def by_name(t):
    t = str.lower(t[0])
    return t

L2 = sorted(L, key=by_name)
print(L2)

#再按成绩从高到低排序：

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score)
print(L2)
