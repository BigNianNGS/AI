# -*- coding: utf-8 -*-
# @Time     :2018/3/1 下午4:44
# @Author   :李二狗
# @Site     :
# @File     :decorator1.py
# @Software :PyCharm

#额外的装饰器

def addTips(i):
    def wrap1(fun):
        def wrap(*args,**kwargs):
             print('这是操作之前')
             result = 0
             if i > 10:
                 result = fun(*args,**kwargs)
             else:
                 print('对不起，没有执行fun的权限')
             print('这个是操作结束')
             return result
        return wrap
    return wrap1

@addTips(11)
def add(x,y):
   return x+y

print(add(2,4))

