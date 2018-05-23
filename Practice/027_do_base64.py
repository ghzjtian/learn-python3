#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开


#写一个能处理去掉=的base64解码函数：
import base64

def safe_base64_decode(s):

    print(len(s) % 4 )
    #如果是 bytes 类型
    if isinstance(s, bytes):
        if len(s) % 4 != 0:
            for i in list(range(4-len(s) % 4)):
                s += b'\x3d'
    # 如果是 str 类型
    elif isinstance(s, str):
        if len(s) % 4 != 0:
            for i in list(range(4 - len(s) % 4)):
                s += '='

    return base64.b64decode(s)



# 测试:
safe_base64_decode('YWJjZA=')
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA='), safe_base64_decode('YWJjZA')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')