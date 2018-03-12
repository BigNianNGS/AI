# -*- coding: utf-8 -*-
# @Time     :2018/3/9 上午11:31
# @Author   :李二狗
# @Site     :
# @File     :matplotlib_15.py
# @Software :PyCharm

import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

# 生成数据
dataOut = np.arange(24).reshape((4, 6))
print(dataOut)

# 保存数据
np.savetxt('data.txt', dataOut, fmt='%.2f')


# 读取数据
data = np.loadtxt('data.txt')
print(data, data.dtype)

# 画图
# 直线图

y = np.random.randint(1, 11, 5)
print(y)

x = np.arange(len(y))
print(x)

plt.plot(x, y, color='r')
plt.show()


# 柱状图

plt.plot(x, y, color='r')
plt.bar(x, y, color='g')
plt.show()

# 饼状图
# 默认 6.4 4.8
plt.figure(figsize=(6, 8))
plt.pie(y, explode= [0, 0.2, 0, 0, 0])
plt.show()


plt.figure(figsize=(6, 8))
labels = ['part 1', 'part 2', 'part 3']
data = [60, 30, 30]
colors = ['red', 'yellow', 'blue']
explode = [0, 0.05, 0]
plt.pie(data, explode=explode, labels=labels, colors=colors, labeldistance=0.8)
plt.axis('equal')
plt.legend()
plt.show()