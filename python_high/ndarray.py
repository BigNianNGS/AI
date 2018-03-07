# -*- coding: utf-8 -*-
# @Time     :2018/3/7 上午9:34
# @Author   :李二狗
# @Site     :
# @File     :ndarray.py
# @Software :PyCharm

import numpy as np

print(np.__version__)
# 生成方式 8种
# array  zeros  ones empty  arange linspace logspace random

# array
a = np.array([[2, 3, 4], [5, 6, 7]], dtype=np.float)
print(a)
print(a.dtype)

# zeros

b = np.zeros(3)
print(b)

b1 = np.zeros((3, 4, 2),dtype=np.int)
print(b1)

# ones
c = np.ones((2, 3))
print(c)

# empty
d = np.empty((2, 4))
print(d)

# arange

e = np.arange(3, 10, 2)
print(e)
# 等价
print(np.array(range(3, 10, 2)))

# linspace  等差数列

f = np.linspace(1, 10, 5)
print(f)

f1 = np.linspace(1, 10, 7, endpoint=False)
print(f1)

print(np.linspace(1, 10, 8))


# linspace 等比数列
g = np.logspace(1, 3, 3, endpoint=True, base=2, dtype=np.int)
print(g)

#random

h = np.random.random((2, 3,4))
print(h)
# 等价
print(np.random.randint(1, 5, (2, 3, 4)))


print('属性', h.dtype, h.shape, h.size)