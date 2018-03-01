# -*- coding: utf-8 -*-
# @Time     :2018/2/28 下午5:30
# @Author   :李二狗
# @Site     :
# @File     :oo3.py
# @Software :PyCharm


# 静态方法 类方法
# 1.调用哪些属性
# 2.如何调用

class People():

    country = 'china'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        print('我是实例方法--%s'%self.name)

    #静态方法，不能调用，不能调用实例属性
    @staticmethod
    def ss():
        print('我是静态方法---%s'%People.country)

    #类方法，只能调用类属性，不能调用实例属性
    @classmethod
    def cc(cls):
        print('我是类方法---%s'%cls.country)

p1 = People('lichan',29)

#实例调用
p1.get_name()

#通过类来调用实例方法
People.get_name(p1)


#调用静态方法 使用类名调用
# p1.ss()
People.ss()

#调用类方法，使用类名调用
People.cc()



