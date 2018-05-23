#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开
#利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    i = [ 0 ]
    def counter():
        i[ 0 ] = i[ 0 ] + 1
        return i[ 0 ]
    return counter



# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
