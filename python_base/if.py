
cars = ['audi','benchi','bmw','toyata']
print(cars)

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
			
print(cars)

print('--------------')


car = '1bmw'

print(car != 'bmw')

age = 20

print(age > 10)


# and  or

print(age == 120 or car == 'Nmw')


if age > 18 or age < 130:
	print('18-30')
	

# in 
if car in cars:
	print('in')
else:
	print('not in')
	

if age > 10:
	print('>10')
elif age < 22:
	print('<22')
else:
	print('other')	

lists = []
for item in lists:
	print(item)
	

if lists:
	print('not null')
else:
	print('null')
