#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开

from functools import reduce

CHAR_TO_FLOAT = {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.': -1}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        #//检测到后面的那个数为 小数点
        if n == -1:
            point = 1
            return f
        #前面的正数的计算
        if point == 0:
            if f == -1:
                f = 0.1
                point = 10
                return f
            return f * 10 + n
        #后面的小数的计算
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
