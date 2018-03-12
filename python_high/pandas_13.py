# -*- coding: utf-8 -*-
# @Time     :2018/3/8 上午11:31
# @Author   :李二狗
# @Site     :
# @File     :pandas_13.py
# @Software :PyCharm

import numpy as np
import pandas as pd


# 数据获取
# pd.read_csv()
# pd.read_excel()
# pd.read_json()

#数据过滤

# DataFrame 数据切片
# pandas 处理 Nan 缺省值
# 1 isnull
# 2 notnull

# 3 dropna()
# 4 fillna()

dict1 = {
    '语文': [90, 88, 67],
    '数学': [91, 89, 68],
    '外语': [92, 90, 69],
    '物理': 100,
}

df2 = pd.DataFrame(dict1)

df2['数学'][1] = np.nan

#df2.ix['数学'] = np.nan

print(df2)

# any 删除所有有 nan的 行
# all 删除行所有字段都是 nan的

#axis =0 删除 行  =1 删除列
print(df2.dropna(how='any', axis=1))


df3 = pd.DataFrame(np.random.random((7, 3)))

print(df3)

df3.ix[:4, 1] = np.nan

df3.ix[:2, 2] = np.nan

print(df3)

print(df3.fillna('123'))

# 不同列进行不同的默认值设置
#print(df3.fillna({1: 0.5, 2: 1}))


print(df3.describe())

# 中位数
print(df3.median())

# 方差
print(df3.var())

# 标准差
print(df3.std())

# 相关系数
print(df3.corr())

# 协方差
print(df3.cov())

print('---------------')
#
s1 = pd.Series(['a', 'b', 'c', 'a', 'b'])

print(s1.unique())

print(s1.value_counts())

df4 = pd.DataFrame(np.random.randint(10, 16, (3, 3)), columns=['a', 'b', 'c'])
print(df4)
print(df4['a'].unique())

# 出现的频率
print(df4['a'].value_counts())

print(s1.isin(['100']))