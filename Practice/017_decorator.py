#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

import time, functools


def metric(fn):
    @functools.wraps(fn)
    def f1(args, **kw):
        bt=time.time()
        fn(args, kw)
        et=time.time()
        print('%s executed in %s ms' % (fn.name, et-bt))
        return fn(*args, kw)
    return f1


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功!')
