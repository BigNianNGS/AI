
# if python2
# class Dog(object):
class Dog():
	"""构造方法"""
	def __init__(self,name,age,weight=5):
		self.name = name
		self.age = age
		self.weight = weight
		# ~ return self  不需要，程序已经内设
		
	def set_weight(self,weight):
		self.weight = weight
	
	def eat_bone(self):
		print(self.name + 'is eating bone')
		
	def bark(self):
		print(self.name+' is barking')
		
	def get_string(self):
		print('my name is '+ self.name+',my age is '+ str(self.age))
			


#初始化 对象  并调用
my_dog = Dog('lichan\'dog',10,90)

#1 修改属性
my_dog.name = 'other'

#2 修改属性 set方法
my_dog.set_weight(100)

#打印属性
print(my_dog.name)

#设置默认属性
print(my_dog.weight)

my_dog.eat_bone()

my_dog.bark()

my_dog.get_string()


print('------')
# ~ 继承
class PetDog(Dog):
	def __init__(self,name,age):
		#if python2
		# super(PetDog,self).__init__(name,age)
		super().__init__(name,age)
		self.food = []
	
	def print_food(self):
		if self.food:
			print(self.food)
		else:
			print('no food')
			
	#重写
	def eat_bone(self):
		print(self.name + 'can not eating bone')
		

	
my_pet_dog = PetDog('my_pet_dog',999)

print(my_pet_dog.name)

my_pet_dog.bark()

my_pet_dog.food = ['a','b','c']

my_pet_dog.print_food()


my_pet_dog.eat_bone()
