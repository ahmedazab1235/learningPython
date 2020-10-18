active = True

while active :
    message = input("enter a pizza toppings you want to add\nenter a 'quit' to End you pizza\n")
    if message == 'quit' :
        active = False
    else:
        print(f"add {message} :)")