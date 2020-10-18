while True :
    age = input("enter your age\nenter quit if you want to close the program\n")

    if age == 'quit' :
        break

    age = int(age)

    if 3 > age > 0:
        print("tiket is free")
    elif 12 >= age >=3 :
        print("the ticket is $10")
    elif age > 12 :
        print("the ticket is $15")
