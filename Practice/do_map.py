#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
#没完成

def normalize(name):
#    return map(toLower,list(name))
#
#def toLower(x):
#    return x

# 测试:
L1 = ['adam', 'LISA', 'barT']
#L2 = list(map(normalize, L1))
L2 = (map(normalize, L1))
print(L2)
