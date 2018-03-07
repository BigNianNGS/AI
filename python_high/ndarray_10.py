# -*- coding: utf-8 -*-
# @Time     :2018/3/7 下午1:52
# @Author   :李二狗
# @Site     :
# @File     :ndarray_10.py
# @Software :PyCharm

import numpy as np

arr = np.array([2, 2, 4, 3, 100])
print(np.abs(arr))

# 开平方  **0.5
print(np.sqrt(arr))

# 平方  **2
print(np.square(arr))

# e 的 x次方
print(np.exp(arr))

arr1 = np.array([-2, 2, 4, 3, 100])
# sign
print(np.sign(arr1))

# modf
arr2 = np.array([-2, 1.2, 2.4, 3.0, 100])
print(np.modf(arr2))

# isnan  NaN

# 是否为NaN
print(np.nan)

# inf有穷  isinf 无穷的
print(np.inf)

# cos cosh sin sinh tan tanh

#mod 元素级的取模

#greater greater_equal less less_equal equal not_equal

#logical_and、not,or,xor（异或）

#power

print(np.power(arr2, arr2))


#聚合函数 平均值 最大值 最小值  方差


a =np.random.randint(2, 100, (3, 4, 5))
print(a)

print(a.max())
print(a.min())
print(a.sum())
# 平均值
print(a.mean())
# 方差
print(a.std())

print('------------')
# 针对某一行进行处理
f = np.array([[1, 2, 3, 4, 5], [3, 4, 5, 6, 7]])

print(f.max(axis=0))


# 三元函数

a1 = np.array([[3, 5], [2, 8]])
b1 = np.array([[1, 6], [4, 3]])

condition = a1 > b1
print(np.where(condition, a1, b1))

print('-------')
c = np.array([[2, 3, np.nan], [4, 5, 7], [np.inf, np.nan, 22]])

print(c)

condition1 = np.isnan(c) | np.isinf(c)
print(np.where(condition1, 0, c))


# 数据去重 unique
print('数据去重')

