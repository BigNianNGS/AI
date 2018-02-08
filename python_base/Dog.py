

		

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
			

#对象初始化子对象
class Family():
	def __init__(self,dad,mama):
		self.dad = dad
		self.mama = mama
		self.brother = []
	
	def get_dad(self):
		return self.dad
		
	def get_mama(self):
		return self.mama
		
		
# ~ 继承
class PetDog(Dog):
	def __init__(self,name,age):
		#if python2
		# super(PetDog,self).__init__(name,age)
		super().__init__(name,age)
		self.food = []
		self.family = Family('lichan','lidewife')
	
	def print_food(self):
		if self.food:
			print(self.food)
		else:
			print('no food')
			
	#重写
	def eat_bone(self):
		print(self.name + 'can not eating bone')
		

