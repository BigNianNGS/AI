

# raw_input for ~2.x  input for 3.x

# ~ msg = input('please input your name:')

# ~ print(msg)

# ~ print(type(msg))

# ~ age = input('please input your age:')

# ~ if int(age) > 20:
	# ~ print('old man')
# ~ else:
	# ~ print('fresh man')


# while 循环

counter = 1

while counter <= 5:
	print(counter)
	counter+=1
	
print('while end')


active = True

# ~ while active:
	# ~ msg = input('请输入信息：')
	# ~ if msg == 'quit':
		# ~ active = False
	# ~ else:
		# ~ print(msg)

# ~ print('while end2')

# break countiune


# break 跳出循环  continue 结束本次循环

counter2 = 1

while counter2 <= 10:
	counter2+=1
	if(counter2%5 == 0):
		continue
	print(counter2)
	
cars = ['bwm','bchi','nassi','bwm']
cars2 = []
cars3 = []

for car in cars:
	cars2.append(car)
print(cars2)
print(cars3)

while cars:
	poped = cars.pop()
	cars3.append(poped)

#cars = null
print(cars)

# cars3 != null
print(cars3)

# 删除列表的元素 并没有.removeall的用法

cars3.remove('bwm')
print(cars3)
	
while 'bwm' in cars3:
	cars3.remove('bwm')

print(cars3)
		
	
students = {}
doing = True
while doing:
	name = input('请输入学生的名字:')
	age = input('请输入学生的年龄:')
	students['name'] =  name 
	students['age'] = age
	
	is_continue = input('还需要继续输入么？')
	if is_continue == 'no':
		doing = False

print('input end')

print(students)



