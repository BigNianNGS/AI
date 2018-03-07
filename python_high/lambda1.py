# -*- coding: utf-8 -*-
# @Time     :2018/3/1 下午6:21
# @Author   :李二狗
# @Site     :
# @File     :lambda1.py
# @Software :PyCharm

#基本函数
def fun1(x,y,z):
    return x+y+z

print(fun1(1,2,3))



result = []

for i in range(8):
    result.append(i**2)

print(result)

#匿名函数

print([i**2 for i in range(8)])

print([i for i in range(9) if i%2 == 0])

#二纬列表
a = [[1,2,3],[44,55,66],[77,88,99]]
print(a)

#嵌套
print([j for i in a for j in i])
