'''
第一题：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
'''

# ~ while(1):
	# ~ score = input('请输入成绩(q for quit):')
	# ~ if score == 'q' or score == 'quit':
		# ~ break
	# ~ score_int = float(score)
	# ~ if(score_int >= 90):
		# ~ print('A')
	# ~ elif(score_int >= 60):
		# ~ print('B')
	# ~ else:
		# ~ print('C')


# score = int(input('请输入你的成绩分数：'))
# if score >= 90:
#     print('成绩为A')
# elif score >= 60 and score < 90:
#     print('成绩为B')
# else:
#     print('成绩为C')

'''
第二题：for 
    创建一个名为favorite_places的字典。
    在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1〜3个地方. 
    朋友指出一个名字(input)。遍历这个字典，并将输入名字及其喜欢的地方打印出来
    还可以继续输入名字 如果输入q则退出
#创建字典
favorite_places = {'张三':['上海','北京','广州'],'李四':['九寨沟','张家界','鼓浪屿'],'东方耀':['长沙', '上海', '深圳']}
'''
# ~ favorite_paces = {
	# ~ '张三':['上海','北京','广州'],
	# ~ '李四':['九寨沟','张家界','鼓浪屿'],
	# ~ '张dk':['长沙', '上海', '深圳'],
	# ~ }

# ~ flag = True

# ~ while(flag):
	# ~ username = input('请输入名字(q for quit):')
	# ~ if username == 'q' or username == 'quit':
		# ~ flag = False
		# ~ continue  
		# ~ #break is ok here
	# ~ places = favorite_paces[username]
	# ~ print(username + ' 喜欢去的地方分别是 '+ '、'.join(places))
	

'''
第三题：
99乘法表 
   用for循环打印99乘法表
   用while
   1x1 =1
   1x2 = 2 2x2 = 4
'''

# ~ start_num = 1
# ~ while(start_num <= 9):
	# ~ second_num = 1
	# ~ while(second_num <= start_num):
		# ~ print(str(second_num)+ '*'+str(start_num) +'='+ str(second_num * start_num), end=' ')
		# ~ second_num+=1
	# ~ start_num+=1
	# ~ print('')
	
for i in range(1, 10):  
	for j in range(1, i+1):
		print('%dX%d=%d'%(j,i,(i*j)), end=' ')	
	print()
	
'''
第四题：
1-100的和
    1+2+3+4+...+100 = ?
    range(1,101)
'''

# ~ total_sum = 0
# ~ for item in range(1,101):
	# ~ total_sum += item
	
# ~ print('1-100的和为'+ str(total_sum))


'''
第五题：
从键盘输入一个字符串，将小写字母全部转换成大写字母,
    将字符串以列表的形式输出(如果字符串包含整数,转为整型)?
'''
#todo
# ~ string  = input('请输入字符串（q or quit for end）：')
# ~ string2 = string.encode('gbk')  
# ~ print (string.upper())
# ~ num_string = filter(string.isdigit,string2)
# ~ print (num_string)
