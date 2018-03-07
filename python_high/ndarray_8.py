# -*- coding: utf-8 -*-
# @Time     :2018/3/7 上午10:01
# @Author   :李二狗
# @Site     :
# @File     :ndarray_8.py
# @Software :PyCharm

import numpy as np

a = np.array([2999, 3, 4], dtype=np.string_)
print(a, a.dtype)


c = np.array(['python123456', 'java', 'rn'], dtype='U4')
print(c, c.dtype)

d = np.random.random((2, 5, 3))
print(d, d.shape)

# d.shape = (3, 10)
# print(d, d.shape)

# copy 原数据保持不变
e = d.reshape((3, 10))
print(e, e.shape)

print(id(d[0][0][0]), id(e[0][0]))
# 4493132232 4493132232


# 数组运算  追加
a1 = [2, 3, 5]
b1 = ['22', '66', 99]
print(a1+b1)

#数据矢量化运算  维度相同
a = np.array([2, 3, 5])
b = np.array([4, 6, 1])
print(a+b)

c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[1, 2, 3], [4, 5, 6]])
print((c+d)**2)

d.shape = (3, 2)
#点乘
print(c,d)
print(np.dot(c, d))
print(c.dot(d))






