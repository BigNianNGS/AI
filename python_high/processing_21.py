# -*- coding: utf-8 -*-
# @Time     :2018/3/12 下午4:41
# @Author   :李二狗
# @Site     :
# @File     :processing_21.py
# @Software :PyCharm

import time
import multiprocessing
import queue
import threading


# 进程间通信   发消息 数据
# 队列 管道  Queue Pipe

#put get

# queue 实现跨进程通信


# def put(q):
#     for value in ['a', 'b', 'c']:
#         print('发送 %s 到 queue 中'%value)
#         q.put(value)
#         time.sleep(2)
#
# def get(q):
#     while True:
#         value = q.get(True)
#         print('从queue 取到数据：%s'%value)


# q = multiprocessing.Queue()
#
# pwrite = multiprocessing.Process(target=put, args=(q, ))
# pread = multiprocessing.Process(target=get, args=(q, ))
#
# pwrite.start()
# pread.start()
#
# pwrite.join()
# pread.terminate()

print('父进程结束')

# Pipe 方法 返回 conn1 conn2, 代表管道的两端
# 前收 后 发

def put(p):
    for value in ['a', 'b', 'c']:
        print('发送 %s 到 queue 中'%value)
        p[1].send(value)
        time.sleep(2)

def get(p):
    while True:
        value =  p[0].recv()
        print('从queue 取到数据：%s'%value)

p = multiprocessing.Pipe(duplex=False)

pwrite = multiprocessing.Process(target=put, args=(p, ))
pread = multiprocessing.Process(target=get, args=(p, ))

# pwrite.start()
# pread.start()
#
# pwrite.join()
# pread.terminate()



# 线程之间通信

# 操作心痛课程  生产者与消费者模式

q1 = queue.Queue(maxsize=10)

def producter(name):
    count = 1
    while True:
        q1.put('骨头%s'%(count))
        print('%s生产了骨头',name)
        count+=1
        time.sleep(0.5)

def consumer(name):
    while True:
        print('[%s] 消费 [%s]'%(name, q1.get()))
        time.sleep(1)


p1 = threading.Thread(target=producter, args=('lichan', ))
c1 = threading.Thread(target=consumer, args=('liruo', ))
c2 = threading.Thread(target=consumer, args=('ermao1', ))

p1.start()
c1.start()
c2.start()





