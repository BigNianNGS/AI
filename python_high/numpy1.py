# -*- coding: utf-8 -*-
# @Time     :2018/3/1 下午3:44
# @Author   :李二狗
# @Site     :
# @File     :numpy1.py
# @Software :PyCharm

import numpy as np
#科学计算
from scipy import linalg

#表格计算
import pandas as pd

print(np.arange(10))

for i in range(4):
    print(i)

a = [1,2,4,6,10]
b = []
for i in a:
    b.append(i**2)
print(b)

a = np.arange(6)
print(a)
print(a**2)

print('------')
a = np.array([[1,2],[3,4]])
print(a)

print(linalg.det(a))

s = pd.Series([2,4,6,8,10,np.nan,12])

print(s)

# 0     2.0
# 1     4.0
# 2     6.0
# 3     8.0
# 4    10.0
# 5     NaN
# 6    12.0
# dtype: float64


dates = pd.date_range('20171201',periods=7)
print(dates)

df = pd.DataFrame(np.random.randn(7,4),index=dates,columns=list('ABCD'))

print(df)


#                    A         B         C         D
# 2017-12-01 -0.886268 -1.165175 -0.763444 -0.531230
# 2017-12-02 -1.382017 -0.397219  1.085159  1.067763
# 2017-12-03  1.176144  1.242904  0.625918  0.584256
# 2017-12-04 -1.215724  0.967298  0.006069  0.434232
# 2017-12-05  1.239929 -0.239074 -0.609966 -0.227495
# 2017-12-06 -1.645849  0.140782  0.886827  1.501559
# 2017-12-07  1.488521  0.406653  0.277591  1.001143

#转置
# print(df.T)

#以B这一列排序
print(df.sort_values(by='B'))