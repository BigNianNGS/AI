# -*- coding: utf-8 -*-
# @Time     :2018/3/8 上午10:42
# @Author   :李二狗
# @Site     :
# @File     :DataFrame_12.py
# @Software :PyCharm

import numpy as np
import pandas as pd

# 二维数组 创建 DataFrame

arr = [['lichan', 100], ['zhangsan', 90], ['lisi', 99]]
df1 = pd.DataFrame(arr)

print(df1)

print(df1.dtypes)

print(df1.index)

print(df1.columns)

df2 = pd.DataFrame(arr, index=['第一行', '第二行', '第三行'], columns=['name', 'score'])

print(df2)

# 字典创建

dict1 = {
    '语文': [90, 88, 67],
    '数学': [91, 89, 68],
    '外语': [92, 90, 69],
    '物理': 100,
}

df3 = pd.DataFrame(dict1)

df3.index = ['li', 'wang', 'zhao']

print(df3)



# 获取数据  取列

print(df3['语文']['li'])
# =
print(df3['语文'][0])

print(df3.ix['li']['语文'])

print(df3.ix[:2, :2])


df3.ix['li']['语文'] = np.e

print(df3)
