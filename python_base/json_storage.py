
'''
保存 json文件
dump  as srite
load  as read 
'''
import json


# ~ nums = [2,3,4,5,6,7,8,9,9]

# ~ filename = 'nums.json'

# ~ with open(filename,'w') as w_obj:
	# ~ json.dump(nums,w_obj)

# ~ with open(filename,'r') as r_obj:
	# ~ json = json.load(r_obj)

# ~ print(json)


# ~ filename2  = 'username.json'

# ~ try:
	# ~ with open(filename2,'r') as r_obj:
		# ~ username = json.load(r_obj)
# ~ except FileNotFoundError:
	# ~ username = input('please input your name:')
	# ~ with open(filename2,'w') as w_obj:
		# ~ json.dump(username,w_obj)
		# ~ print('we already rememmer your name')
# ~ else:
	# ~ print('welcome come back: '+username)


#重构  使代码更加的清晰  并且容易理解 容易扩展



def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename,'r') as r_obj:
			username = json.load(r_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		
def write_into_username():
	username = input('please input your name:')
	filename2 = 'username.json'
	with open(filename2,'w') as w_obj:
		json.dump(username,w_obj)
		return username
	
def great_user():
	username = get_stored_username()
	if username:
		print('welcome back ' + username)
	else:
		username = write_into_username()
		print('we already rememmer your name'+ username)
				
great_user()
