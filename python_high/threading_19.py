# -*- coding: utf-8 -*-
# @Time     :2018/3/12 下午3:07
# @Author   :李二狗
# @Site     :
# @File     :threading_19.py
# @Software :PyCharm

import time
import threading

# 多任务  并发运行： 进程 线程
# 时间片 cpu时间  0.01s 1s

def music(name, loop):
    for i in range(loop):
        print('在听音乐:%s 时间：%s  name:%s  id: %s'%(name, time.ctime(), t1.getName(),t1.ident))
        time.sleep(1)

def movie(name, loop):
    for i in range(loop):
        print('在看定影:%s 时间：%s name:%s id: %s'%(name, time.ctime(), threading.Thread.getName(t2), t2.ident))
        time.sleep(1)


# music('模特', 3)
# movie('速度8', 4)
# print('任务结束')       `


t1 = threading.Thread(target=music, args=('模特', 3))
t1.setName('music thread')

t2 = threading.Thread(target=movie, args=('速8', 4), name='movie thread')

# 设置线程守护
t1.setDaemon(True)
t2.setDaemon(True)

# t1.start()
# t2.start()
#
# # 阻塞主线程
# t1.join(1)
# t2.join(1)

#主线程
print('任务结束')


# 加锁

balance = 0

lock = threading.Lock()

def change(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(10000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()

# run_thread(8)

t3 = threading.Thread(target=run_thread, args=(4, ))
t4 = threading.Thread(target=run_thread, args=(8, ))

t3.start()
t4.start()

t3.join()
t4.join()

print(balance)




