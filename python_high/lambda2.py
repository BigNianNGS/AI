# -*- coding: utf-8 -*-
# @Time     :2018/3/1 下午6:28
# @Author   :李二狗
# @Site     :
# @File     :lambda2.py
# @Software :PyCharm

from  functools import  reduce

#lambda 表达式 和 map  reduce  filter 的组合使用

lambda1 = lambda x: x**2

lambda2 = lambda x, y: x+y

lambda3 = lambda x: x % 2 == 0

print(list(map(lambda1, range(8))))


print(reduce(lambda2, range(8)))

print(list(filter(lambda3, range(8))))


#练习
#计算 5!+4!+3!+2!+1!

lambda4 = lambda x, y: x * y

number = reduce(lambda4, range(1, 6))
print(number)
score = 0
for i in range(2, 7):
    tempnumber = reduce(lambda4, range(1, i))
    print(tempnumber)
    score = score + tempnumber

print(score)

lambda5 = lambda n: reduce(lambda4, range(1, n + 1))

print((list(map(lambda5, range(1, 6)))))

lambda6 = lambda a, b: a + b

print(reduce(lambda6, list(map(lambda5, range(1, 6)))))


