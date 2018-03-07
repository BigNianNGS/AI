# -*- coding: utf-8 -*-
# @Time     :2018/3/2 下午2:59
# @Author   :李二狗
# @Site     :
# @File     :time.py
# @Software :PyCharm

from datetime import datetime
import time


print(datetime.now())
#   2018-03-02 15:00:54.548303

#   时间戳  1970.1.1 到现在的秒数
print(time.time())
#   1519974054.5483289

# 时间元祖
print(time.localtime())
# time.struct_time(tm_year=2018, tm_mon=3, tm_mday=2, tm_hour=15, tm_min=2, tm_sec=11, tm_wday=4, tm_yday=61, tm_isdst=0)

# %Y %y %m %d %H %M %S
print(time.strftime('%Y/%m/%d %H:%m:%S', time.localtime()))
time_tuple = time.strptime('2018-03-02 15:00:54', '%Y-%m-%d %H:%M:%S')
print(time.mktime(time_tuple))