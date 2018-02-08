
# 列表 有顺序的 元素的集合
# 

lists = [1,'str',"hello",[1,2,2,2,2,2,2,23],1.0,True,'7890']

name = ['zhangsan','disi']

cars = ['car1','car2']

print(lists)

#列表的访问

lists[0] = 'lichan'

print(lists[0])

print(lists[len(lists)-1])

print(lists[-1])

print(lists[-2])

# 负数下标  从最后开始

#追加
lists.append(900)
print(lists[-1])

lists.insert(1,'900')

print(lists)

del lists[2]

print(lists)


lists.pop()

print(lists)


list1 = lists[3]

list1.pop()

list1.remove(2)


print(lists)

#清空列表

#lists = []

del lists[:]

print(lists)

#列表排序

print('---------')

names = ['lichan','teng yufeng','erha','A','a','b','B']

#print(names)

#正序
#names.sort()

#反序
#names.sort(reverse = True)

#临时排序
#temp_names = sorted(names)

#print(temp_names)

rever = names.reverse()

print(rever)

print(names)






