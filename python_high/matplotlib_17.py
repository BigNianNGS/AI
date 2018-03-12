# -*- coding: utf-8 -*-
# @Time     :2018/3/12 下午2:18
# @Author   :李二狗
# @Site     :
# @File     :matplotlib_17.py
# @Software :PyCharm

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# 中文显示
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'SimHei'
# 负号
mpl.rcParams['axes.unicode_minus'] = False


# x = np.arange(-5, 5)
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y = np.sin(x)
print(x, y)

help(plt.plot)
plt.plot(x, y, color='r', linestyle='--', marker='o')
#plt.xlim(-5, 5)
#plt.ylim(-5, 5)
plt.xlabel(u'我是x轴')
plt.ylabel(u'我是y轴')
plt.xticks(np.arange(-5, 6))
plt.yticks(np.arange(-5, 6))

plt.title(u'我是标题')
plt.text(-3, -3, '$y=sin(x)$', fontsize=20, bbox={'facecolor': 'yellow'})
# 图例
# plt.legend()

# 保存图片
plt.savefig('image.png', dpi=200)
plt.show()

