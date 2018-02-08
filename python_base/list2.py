lists = ['sijie','eee',23,46,True,'a','B']

#循环体  循环外
for item in lists:
	print(item)			
print('for in middle')	
print ('end')


for num in range(1,10):
	print(num)
	
print('---------')

for num in range(1,10,2):
	print(num)

nums = list(range(1,10))

print(type(nums))

print(type(range(1,4)))

squares = []
for var in range(1,11):
	square = var**2
	squares.append(square)
	
print(squares)


print('----------')

#列表解析
newlists = [value**2 for value in range(1,11)]

print(newlists)

#数值计算
print(max(newlists))
print(min(newlists))
print(sum(newlists))


#处理部分元素 切片
print('----------')

print(lists)

#print(lists[2:])

print(lists[-3:])

#列表复制

newlists = lists[:]

print(newlists)

a = [1,2,3]
b = [4,5,6]

#会影响C
c = a

#不会影响C
#c = a[:]
a.append(10)

print(a)
print(c)


print('----------')


#元祖  tuple 特殊的列表，不可变的列表  () []  {}

tuple_a = (1,2,3)

#tuple_a[0] = 100

print(tuple_a)


for temp in tuple_a:
	print(temp)
	


