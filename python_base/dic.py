
#键值对,无序
dic = {
	'name':'lichan',
	'age':20,
	'phone':'18888854481',
	'boy':True,
	20:10,
	True:'ok'
	}
	
dic['age'] = 99
dic[20] = 100
#dic[True] = 0

#删除
#del dic['age']

print(dic)


#遍历

for key,value in dic.items():
	print(str(key) +' '+ str(value))

#  =  for key in dic.keys()


dics = {
	'li':100,
	'wang' : 30,
	'zhao' : 90,
	'zhao':90,
	'A' : 40,
	}

for key in sorted(dics.keys(),reverse = True):
	print(key)


for value in dic.values():
	print(value)

print('--------')
for age in set(dics.values()):
	print(age)
print('--------')

friends = []

for counter in range(0,30):
	friend = {'name':'xxx','age':20}
	friends.append(friend)

for friend in friends[:5]:
	print(friend)

print('total number of friends:'+ str(len(friends)))


print('--------')

#字典嵌套
dic2 = {'name':'lichan','age':'28','study':['yuwen','shuxue']}

print(dic2)

print(dic2['study'])


