
class People():
		#类属性，可以通过类名|实例对象修改
		country = 'china'
		
		#实例属性，只能通过实例对象修改
		def __init__(self,name,age,sex):
			self.name = name
			self.age = age
			self.sex = sex
			
		def getName(self):
			return self.name 


p1 = People('lichan',28,'male')

p1.country = 'hello'

p2 = People('lichan',28,'male')

print(p1.country)

print(p2.country)

print(p1.name)


#获得属性
print(getattr(p1,'name'))

#判断是否有属性
print(hasattr(p1,'name'))

#删除属性
delattr(p1,'name')

#打印属性
print(People.__dict__)

print(p1.__dict__)
