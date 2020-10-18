dinner_list = ['ahmed', 'mohamd', 'azab']


print(f"{dinner_list[2]} can not come" )

dinner_list[2] = 'alaa'

print("i found a biger table")

dinner_list.insert(0,'eslam')

dinner_list.insert(2,'amr')

dinner_list.append('lolo')

print(f"i invite you to dinner ,{dinner_list[0]} !")

print(f"i invite you to dinner ,{dinner_list[1]} !")

print(f"i invite you to dinner ,{dinner_list[2]} !")

print(f"i invite you to dinner ,{dinner_list[3]} !")

print(f"i invite you to dinner ,{dinner_list[4]} !")

print(f"i invite you to dinner ,{dinner_list[5]} !")

print("i can invite only two people")

message = dinner_list.pop()

print(f"i am sorry i can not invite you ,{message} !")

message = dinner_list.pop()

print(f"i am sorry i can not invite you ,{message} !")

message = dinner_list.pop()

print(f"i am sorry i can not invite you ,{message} !")

message = dinner_list.pop()

print(f"i am sorry i can not invite you ,{message} !")

print(f"you are still invited ,{dinner_list[0]} !")

print(f"you are still invited ,{dinner_list[1]} !")

del dinner_list[1]

del dinner_list[0]

print(dinner_list)
