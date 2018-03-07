# -*- coding: utf-8 -*-
# @Time     :2018/3/7 下午2:38
# @Author   :李二狗
# @Site     :
# @File     :pandas_11.py
# @Software :PyCharm

import numpy as np
import pandas as pd

# numpy ndarray

# pandas  一维数组 序列 Series  数组 DataFrame

arr = np.random.randint(10, 20, (3, 4))
print(arr)

arr1 = np.array([22, 33, 44, 55])
print(arr1)
s1 = pd.Series(arr1)
print(s1)
# 0    22
# 1    33
# 2    44
# 3    55
print(s1.dtype)
print(s1.index)
print(s1.values)

# 修改索引
s1.index = ['a1', 'a2', 'a3', 'a4']
print(s1)
# a1    22
# a2    33
# a3    44
# a4    55

# 索引可以重复

s2 = pd.Series(data=[1, 2, 3], index=['a', 'b', 'c'], dtype=np.int)
print(s2)

dict1 = {'语文': 1, '数学': 2, '外语': 100}

s3 = pd.Series(dict1)

print(s3)

# key
print(s3['语文'])
# index
print(s3[0])

# 切片
print(s3['数学':])

print(s3[1:])


# 运算
print(s3**2)

print(s3+s3)

s4 = pd.Series(s3, index=['外语', 'b', 'c', 'd'])
print(s4)

s4[pd.isnull(s4)] = -1

print(s4)


# 自动对齐