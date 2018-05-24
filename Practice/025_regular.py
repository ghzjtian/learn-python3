#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开


import re

#1.验证出类似的Email：

def is_valid_email(addr):
    # return True
    return re.match(r'^[\w_.]+@[\w_.]+.\w+$', addr)



# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok1')


# 二可以提取出带名字的Email地址：

def name_of_email(addr):
    return re.match(r'<?([a-zA-Z\s]*)[a-zA-Z>\s]*@[\w_.]+.\w+$', addr).group(1)


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok2')


addr = 'someone@gmai@l.com'
# m = re.match(r'^[\w_.]+@([\w_.]+?).(\w+)$', addr)
m = re.findall(r'@([\w_.]+?)',addr)
print(m)
