# -*- coding: utf-8 -*-
# @Time     :2018/3/9 下午2:51
# @Author   :李二狗
# @Site     :
# @File     :matplotlib_16.py
# @Software :PyCharm
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from  matplotlib import rcParams
import pandas as pd

# 中文显示
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'SimHei'
# 负号
mpl.rcParams['axes.unicode_minus'] = False

#print(mpl.matplotlib_fname())


# plt.figure(figsize=(6, 8))
# labels = ['第一部分', '第二部分', '第三部分']
# data = [60, 30, 30]
# colors = ['red', 'yellow', 'blue']
# explode = [0, 0.05, 0]
# plt.pie(data, explode=explode, labels=labels, colors=colors, labeldistance=0.8)
# plt.axis('equal')
# plt.legend()
# plt.show()



# 箱形图 数据分析
df1 = pd.DataFrame({
    u'计算机应用基础': [85, 78, 81, 95, 70, 67, 82, 72, 80, 81, 77],
    u'西方经济学': [93, 81, 76, 88, 66, 79, 83, 92, 78, 86, 78],
    u'数学': [65, 95, 51, 74, 78, 63, 91, 82, 75, 71, 55],
    u'英语': [76, 90, 97, 71, 70, 93, 86, 83, 78, 85, 81],
})

# print(df1)
# df1.describe()
# df1.boxplot()
# plt.show()


plt.boxplot(x=df1.values,labels=df1.columns)
plt.ylim(0, 85)
plt.style.use('ggplot')
plt.show()