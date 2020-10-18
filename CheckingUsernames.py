current_users = ['ahmed', 'essam', 'azab', 'omer', 'eslam']

new_users = ['ahmed', 'essam','mohamed', 'cotineo']

for newuser in new_users:
	if newuser.lower() in current_users:
		print('that the person will need to enter a new username')
	else: 
		print('that the username is available')