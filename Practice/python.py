#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#要把该文件的权限改为  chmod a+x  ,才能双击打开


print('hello,world!')
print('100+200=',100+200)
#name = input('please enter your name: ')
#print('hello',name)

print(r'''line1
    line2
    line3''')

n = 123
f = 456.789
s1 = 'Hello,world'
s2 = 'Hello,\'Adam\''
s3 = r'Hello,"Bart"'
s4 = r'''Hello,
    Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

print('天')

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print ('%.1f%%' % r)

classmates = ['Michael','Bob','Tracy']
print(classmates)

height = 1.75
weight = 80.5

bmi = weight/(height*height)

if  bmi < 18.5 :
    print('过轻!')
elif  bmi < 25 :
    print('正常!')
elif  bmi < 28 :
    print('过重!')
elif  bmi < 32 :
    print('肥胖!')
else :
    print('严重肥胖')


n1 = 255
n2 = 1000

print(hex(n1))
print(hex(n2))


def my_abs(x):
    if  not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>= 0:
        return x
    else:
        return -x

print(my_abs(-99))

#print(my_abs('A'))

#//定义函数
import math

def quadratic(a,b,c):
    x = (-b + math.sqrt((b*b)-4*a*c))/(2*a)
    y =(-b - math.sqrt((b*b)-4*a*c))/(2*a)
    return x,y

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

# 默认参数
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end([1, 2, 3]))
print(add_end())
print(add_end())

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3))

#

def product(x,y = 1,*numbers):
    sum = x * y
    for n in numbers:
        sum = sum * n
    return sum

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')












