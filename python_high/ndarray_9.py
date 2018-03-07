# -*- coding: utf-8 -*-
# @Time     :2018/3/7 上午11:27
# @Author   :李二狗
# @Site     :
# @File     :ndarray_9.py
# @Software :PyCharm

import numpy as np

a = np.random.random((2, 3, 4))
#print(a)
# print(a[0, 1, 1])
# print(a[0][1][1])

# 切片
#
# print(a[0][0][1:3])

# print(a[0][:][1:3])
# 等价于
# print(a[0, :, 1:3])
#print(a[0][:].T[1:3].T)

# BOOL值的索引
b = np.random.random((4, 4, 2))
print(b)

c = b > 0.5

print(c)

d = b[c]
print(d)

#花式索引

f = np.arange(32).reshape((8, -1))
print(f)
print(f[[0, 3, 5], [0, 3, 2]])

print(f[np.ix_([0, 3, 5], [0, 3, 2])])

# axis0  行
# asis1 列


# 转置

# shape
g = np.arange(24).reshape((2, 3, 4))
print(g)

h = g.T
print(h, h.shape)

# 等价于 T
i = np.transpose(g)
print(i, i.shape)

