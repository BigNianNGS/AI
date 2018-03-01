# -*- coding: utf-8 -*-
# @Time     :2018/2/28 下午5:44
# @Author   :李二狗
# @Site     :
# @File     :copy1.py
# @Software :PyCharm

# 赋值，浅拷贝，深拷贝

# python 可变对象  list dict  不可变对象 string tuple number

str1 = 'lichan'

print(id(str1))

str1 = 'ergou'

print(id(str1))

# 4525139480
# 4526502776

list = [1,2,3,4]

list1 = list

print(id(list))
print(id(list1))

# 4548152648
# 4548152648

list[1] = 22
print(id(list))
print(id(list1))


#浅拷贝
# [:] list()  set() copy.copy() list.copy()

a = [1,2,3]
b = [11,22,33]
c = [111,222,333]

list2 = [a,b,c]
print('list2的内存地址'+ str(id(list2)))

#深拷贝
list3 = list2

print(id(list3) == id(list2))
# True

#浅拷贝
list4 = list2[:]
print(id(list4) == id(list2))
#False

a[0] = 'ergou'
print(list2)
print(list3)
print(list4)

# [['ergou', 2, 3], [11, 22, 33], [111, 222, 333]]
# [['ergou', 2, 3], [11, 22, 33], [111, 222, 333]]
# [1, 22, 3, 4]

list2[0] = 'lichan'

print(list2)
print(list3)
print(list4)

['lichan', [11, 22, 33], [111, 222, 333]]
['lichan', [11, 22, 33], [111, 222, 333]]
[1, 22, 3, 4]


print(id(list2[0][1]))
print(id(list4[0][1]))

# 4326439712
# 4324898160

print(id(list2[0]))
print(id(list4[0]))