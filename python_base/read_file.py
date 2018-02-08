

'''
open 需要 close 
with 关键字：open 之后 系统帮你 close，无需人工close
'''

# ~ #open函数 ('名字','handle')  'r' 缺省值
# ~ with open('data.txt','r') as file_object:
	# ~ contents = file_object.read()
	# ~ print(contents)
	


# ~ #相对路径和绝对路径

# ~ #相对路径
# ~ with open('testfiles/test_data.txt','r') as file_object:
	# ~ contents = file_object.read()
	# ~ print(contents)


#绝对路径 win and mac is diffent for \ /
with open('/Users/liergou/Desktop/AI/python_base/testfiles/test_data.txt','r') as file_object:
	# ~ contents = file_object.read()
	# ~ print(contents)
	# ~ for line in file_object.readlines():
		# ~ print(line.rstrip())
		lines =  file_object.readlines()

for line in lines:
	print(line.rstrip())
