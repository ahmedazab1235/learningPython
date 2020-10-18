lolperson = {'Fname' : 'lol', 'Lname' : 'elhosany', 'age' : '23' , 'city' : 'manshatdmalo'}
ahmedperson = {'Fname' : 'ahmed', 'Lname' : 'azab', 'age' : '23' , 'city' : 'manshatdmalo'}
mohamedperson = {'Fname' : 'mohamed', 'Lname' : 'abas', 'age' : '23' , 'city' : 'manshatdmalo'}

peoples = [lolperson, ahmedperson, mohamedperson]

for people in peoples :
	print(f"full name:{people['Fname']} {people['Lname']}")
	print(f"age is {people['age']}")
	print(f"city is {people['city']}")