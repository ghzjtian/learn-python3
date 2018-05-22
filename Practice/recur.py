#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开
#汉诺塔,
#https://baike.baidu.com/item/%E6%B1%89%E8%AF%BA%E5%A1%94/3468295
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756044276a15558a759ec43de8e30eb0ed169fb11000


def move(n,a,b,c):
    if n == 1:
        #一个的话，直接 a->c.
        print(a,'--->',c)
    else:
         move(n-1,a,c,b)
         move(1,a,b,c)
         move(n-1,b,a,c)


#    elif n==2:
#         #参考1, a->b (把 b ，c 的顺序交换)
#        move(n-1,a,c,b)
##        #然后移动最大的盘子,a->c
##        print(a,'--->',c)
#        move(1,a,b,c)
#        #参考1,b->c(把 a ，b 的顺序交换)
#        move(n-1,b,a,c)



#    elif n ==3 :
#        #参考2,a->b(b,c的顺序交换)
#        move(n-1,a,c,b)
#        #然后移动最大的盘子
#        move(1,a,b,c)
#        #参考2,b->c(a,b的顺序交换)
#        move(n-1,b,a,c)
#
#    elif n==4:
#        #参考3,a->b(b,c的顺序交换)
#        move(n-1,a,c,b)
#        #然后移动最大的盘子
#        move(1,a,b,c)
#        #参考3,b->c(a,b的顺序交换)
#        move(n-1,b,a,c)




# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(2, 'A', 'B', 'C')


