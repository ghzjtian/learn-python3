#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开

def is_palindrome(n):
    str_n = str(n)
    return isSame(str_n)

#检查是否是回数,text 为字符串类型
def isSame(text):
    str_lenth = len(text)
    if str_lenth == 1:
        return True
    
    for x in range(str_lenth):
        if(text[x] != text[str_lenth-1-x]):
            return False
        elif x>str_lenth/2:
            return True
    return True

# 测试:
#print('int 1~10:',list(range(1, 10)))
#print('str 1~10:',list(map(str, list(range(1, 10)))))

      
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

