# -*- coding: utf-8 -*-
# @Time     :2018/2/28 下午6:05
# @Author   :李二狗
# @Site     :
# @File     :copy_in.py
# @Software :PyCharm

#深拷贝
# copy.deepcopy

import copy

a = [1,2,3]
b = [11,22,33]
c = [111,222,333]

list1 = [a,b,c]

list4 = copy.deepcopy(list1)

print(id(list1) == id(list4))
#False

print(id(list1[0]) == id(list4[0]))
#False

print(id(list1[0][1]) == id(list4[0][1]))
#True

a[0] = '1111'
print(list1)
print(list4)
# [[1111, 2, 3], [11, 22, 33], [111, 222, 333]]
# [[1, 2, 3], [11, 22, 33], [111, 222, 333]]


# list[1][0] = '1111'
# print(list1)
# print(list4)