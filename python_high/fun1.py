# -*- coding: utf-8 -*-
# @Time     :2018/3/1 下午4:05
# @Author   :李二狗
# @Site     :
# @File     :fun1.py
# @Software :PyCharm

def fun1():
    def fun2():
        def fun3():
            print('fun3')
        return fun3
        # print('hello world')
    return fun2

fun1()()()