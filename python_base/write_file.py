
filename = 'test_write.txt'

# a 追加  w 重写
with open(filename,'a') as file_object:
	file_object.write('you are right\n')
	file_object.write('dierhang\n')
	
