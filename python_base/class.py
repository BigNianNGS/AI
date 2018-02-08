
class Dog():
	def __init__(self,name,age):
		self.name = name
		self.age = age
		# ~ return self  不需要，程序已经内设
	
	def eat_bone(self):
		print(self.name + 'is eating bone')
		
	def bark(self):
		print(self.name+'is barking')
		
	def get_string(self):
		print('my name is '+ self.name+',my age is '+ str(self.age))
			


#初始化 对象  并调用
my_dog = Dog('lichan\'dog',10)

print(my_dog.name)

my_dog.eat_bone()

my_dog.bark()

my_dog.get_string()

