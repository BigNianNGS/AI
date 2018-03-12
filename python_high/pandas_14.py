# -*- coding: utf-8 -*-
# @Time     :2018/3/9 上午11:06
# @Author   :李二狗
# @Site     :
# @File     :pandas_14.py
# @Software :PyCharm

import numpy as np
import pandas as pd

print(pd.__version__)

s1 = pd.Series([99, 100, 10, 87, 67], index=[['2007', '2007', '2018', '2018', '2018'], ['a', 'b', 'c', 'a', 'c']])

print(s1)

df1 = pd.DataFrame({

})