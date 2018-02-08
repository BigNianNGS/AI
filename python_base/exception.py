
'''
异常处理
'''

# ~ try except else
# ~ print(7/0)

try:
	print(7/1)
except ZeroDivisionError:
	print('error is doing')s
else:
	print('is woring')

# ~ print('please input two numbers:(type q chart quit)')

# ~ while True:
	# ~ num1 = input('\n first number:')
	# ~ if(num1 == 'q'):
		# ~ break
	# ~ num2 = input('\n seconed num:')	
	# ~ if(num2 == 'q'):
		# ~ break
	
	# ~ try:
		# ~ result = int(num1)/int(num2)
	# ~ except ZeroDivisionError:
		# ~ print('被除数不能为0')
	# ~ else:
		# ~ print(result)
	


filename = 'notfind.txt'

try:
	with open(filename,'r') as file_obejct:
		contents = file_object.read()
except FileNotFoundError:
	print('sorry,can not find the file')
	# ~ pass  无任何处理
else:
	print(contents)
