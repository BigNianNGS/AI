# -*- coding: utf-8 -*-
# @Time     :2018/3/12 下午4:09
# @Author   :李二狗
# @Site     :
# @File     :processing_20.py
# @Software :PyCharm

# 多进程

import time
import multiprocessing
import os

# 单进程
def work_1(filename, n, lock):
    print('work1 start')
    lock.acquire()
    for i in range(n):
        with open(filename, 'a') as f_obj:
            f_obj.write('www.baidu.com come on  \n')
            time.sleep(1)
    print('work_1 end')
    lock.release()


# 单进程
def work_2(filename, n, lock):
    print('work——2 start')
    lock.acquire()
    for i in range(n):
        with open(filename, 'a') as f_obj:
            f_obj.write('www.sina.com come on111  \n')
            time.sleep(1)
    print('work-2 end')
    lock.release()


# p1 = multiprocessing.Process(target=work_1,args=('lichan.txt', 3))
# p2 = multiprocessing.Process(target=work_2,args=('lichan.txt', 4))

# p1.start()
# p2.start()

# 同步执行  异步执行

#加锁  同步

lock = multiprocessing.Lock()
p1 = multiprocessing.Process(target=work_1,args=('lichan.txt', 3, lock))
p2 = multiprocessing.Process(target=work_2,args=('lichan.txt', 4, lock))

# p1.start()
# p2.start()



# 进程池 pool

def work(m):
    print('run work(%s) start work id: %s'%(m, os.getpid()))
    time.sleep(1)
    print('work(%s) end work id:%s'%(m, os.getpid()))


print('父进程id %s'%os.getpid())

# 创建一个进程池

pool = multiprocessing.Pool(2)

for i in range(5):
    pool.apply_async(work, args=(i, ))

pool.close()
pool.join()

print('父进程结束')
