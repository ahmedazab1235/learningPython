from random import choice

listof_l_n = [1,2,3,4,5,6,7,8,9,11, 'ahmed', 'essam', 'mohamed','abdelshafy', 'azab']

my_ticket = 5
x = 0

while True :
   ran = choice(listof_l_n)
   if ran == my_ticket :
       print(x)
       print('you won')
       break
   else:
       x +=1

