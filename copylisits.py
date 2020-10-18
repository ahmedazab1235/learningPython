pizzas = ['sopersoprem', 'margreta', 'cheken']

friend_pizzas = pizzas[:]

pizzas.append('perony')

friend_pizzas.append('meat')

print("My favorite pizzas are:")

for pizza in pizzas :

	print(pizza)

print("My friend’s favorite pizzas are:")

for friend_pizza in friend_pizzas :

	print(friend_pizza)