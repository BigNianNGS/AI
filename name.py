# -*- coding: utf-8 -*-
# @Time     :2018/2/27 下午3:32
# @Author   :李二狗
# @Site     :
# @File     :name.py
# @Software :PyCharm


# 封装 继承 多态

class A():
    def a(self):
        print('我是A里面的a方法')

class B():
    def b(self):
        print('我是B里面的b方法')

class C():
    def c(self):
        print('我是C里面的c方法')

class D(A,B,C):

    def __init__(self,name,address):
        self.name = name
        #私有属性
        self.__address = address

    def d(self):
        print('我是D里面的d方法')

#重写C类，多态
    def c(self):
        print('我是D里面的c方法'+ self.__address)

dd = D('lichan','beijing')
dd.a()
dd.b()
dd.c()
dd.d()


#多态
dd.c()

#私有属性
# print(dd.address)
print(dd.name)

# todo
# print(dd.get__address())

#强制访问
print(dd._D__address)
