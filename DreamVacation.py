city = []
active = True

while active :
    message = input("where would you like to go :)\nif you want to end write quit\n")
    if message == 'quit' :
        break
    city.append(message)
for city1 in city :
    print(city1)