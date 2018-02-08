#引入外部方法模块

#1 导入整个文件
#2 加别名
# ~ import func_modules as fm

#3只调用某一个方法
#4 设置别名
from func_modules import add_nums_module as add

#全部导入，直接使用方法 from module import *


#result = func_modules.add_nums_module(1,2,3)
# as  之后不能再使用真名
result = add(1,2,3)

print(result)


