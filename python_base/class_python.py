from collections import OrderedDict

order1 = OrderedDict()

order1['name'] = 'lichan'
order1['age'] = 18

print(order1)


for name,age in order1.items():
	print(name + ' and ' + str(age))
