n = int(input("please enter the numper"))

odd = list(range(1,101,2))

even = list(range(2,101,2))

if n in odd :
    print('Weird')
elif n in even :

    if 2 <= n <= 6:
        print('Not Weird')
    elif 6 <= n <= 20:
        print('Weird')
    elif 21 <= n <= 100:
        print('Not Weird')
 