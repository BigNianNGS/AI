# -*- coding: utf-8 -*-
# @Time     :2018/2/28 下午6:16
# @Author   :李二狗
# @Site     :
# @File     :copy2.py
# @Software :PyCharm

import copy

list_0 = ["A", "B", ["C", "D"], "E"]
list_1 = copy.copy(list_0)
list_2 = list_0.copy()
list_3 = list_0[:]
list_4 = list(list_0)
list_5 = list_0  #指向同一对象 浅拷贝

# --- 深拷贝的拷贝方式 ---
list_d = copy.deepcopy(list_0)

print('list0 -1 地址对比--')
print(id(list_0))
print(id(list_1))

list_0[0] = '改变'

print('list0 -1 [0]地址对比--')
print(id(list_0[0]))
print(id(list_1[0]))
print(id(list_2[0]))
print(id(list_3[0]))
print(id(list_4[0]))
print(id(list_5[0]))
print(id(list_d[0]))

list_0[2][1] = '21改变'
print('list0 -1 [1][0]地址对比--')
print(id(list_0[2][1]))
print(id(list_1[2][1]))
print(id(list_2[2][1]))
print(id(list_3[2][1]))
print(id(list_4[2][1]))
print(id(list_5[2][1]))
print(id(list_d[2][1]))


print('------对比--')
print(id(list_2))
print(id(list_3))
print(id(list_4))
print(id(list_5))
print(id(list_d))


# --- 深浅拷贝与赋值的区别 ---
# 1. 对第一层数据进行赋值
list_0[0] = "X0"
list_1[0] = "X1"
list_2[0] = "X2"
list_3[0] = "X3"
list_4[0] = "X4"
list_5[0] = "X5"
list_d[0] = "Xd"


# 2. 对第二层的list引用进行赋值
# list_0[2][0] = "Y0"
# list_1[2][0] = "Y1"
# list_2[2][0] = "Y2"
# list_3[2][0] = "Y3"
# list_4[2][0] = "Y4"
# list_5[2][0] = "Y5"
# list_d[2][0] = "Yd"


# 3. 对第一层数据进行赋值
# list_0[3]= "Z0"
# list_1[3]= "Z1"
# list_2[3]= "Z2"
# list_3[3]= "Z3"
# list_4[3]= "Z4"
# list_5[3]= "Z5"
# list_d[3]= "Zd"


print(list_0)
print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_5)
print(list_d)