# -*- coding: utf-8 -*-
# @Time     :2018/3/1 下午5:08
# @Author   :李二狗
# @Site     :
# @File     :iterator1.py
# @Software :PyCharm

#迭代器: 排列组合 笛卡尔积 串联迭代器

import itertools

x = range(1,5)
# 排列 从四个里面选三个
com1 = itertools.combinations(x,3)

# for i in com1:
#     print(i)

#组合
com2 = itertools.permutations(x,3)

# for i in com2:
#     print(i)

# 笛卡尔积
y = list('abc')
com3 = itertools.product(x,y)

print(com3)

for i in com3:
    print(i)


#串联迭代器
com4 = itertools.chain(com1,com2,com3)

for i in com4:
    print(i)





# for i in range(9):
#     print(i)

