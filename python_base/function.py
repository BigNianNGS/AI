
def print_hello():
	print('hello')

def print_wel(name):
	"""
	欢迎+name
	"""
	print('hello'+str(name))
	
print_hello()
print_wel(True)


list1 = [2,3,4]

print(sum(list1))

def sum(x,y,z):
	print(x+y+z)


#1位置实参
sum('3','3','5')


# 关键字实参
sum(x=2,z=5,y=4)

sum(2,z=5,y=4)

#任意数量的实参  not_sure_params_sum(param1,*nums)
def not_sure_params_sum(*nums):
	result = 0
	for num in nums:
		result+=num
	return result
	
print(not_sure_params_sum(1,2,3,4,5,6,7))


#任意数量的关键字的实际参数

def create_user(name,age,**params):
	user = {}
	user['name'] = name
	user['age'] = age
	for key,value in params.items():
		user[key]= value 
	return user
		

user1 = create_user('lichan',29,add='beijing',sex='male')
print(user1)
user2 = create_user('liergou',30,xxx='xxx')

print(user2)



#默认值 默认值的参数需要放在后面，默认参数的后面不能有 必传参数
def deault_sum(x,z,y=4):
	print(x+y+z)


deault_sum(100,100)


#有返回值的func
def return_sum(x,y,z):
	result = x+y+z
	return result

print(return_sum(1,2,3))


print('-----------')
# 函数对列表的操作

handle_list = [1,2,3]
# 传递的是 列表的指针，函数会改变列表
def print_list(names):
	names.append(900)
	for name in names:
		print(name)

print_list(handle_list)
print(handle_list)
# 传递列表的copy
print_list(handle_list[:])



def create_student(
		name,
		age,
		sex,
		add
		):
			student = {}
			student['name']=name
			student['age']=age
			student['sex']=sex
			student['add']=add
			return student


stu = create_student('lichan',90,'boy','beijing')
print(stu)
