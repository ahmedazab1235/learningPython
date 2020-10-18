sandwich_orders = ['derger', 'pastrami', 'egg', 'frenshfries', 'pastrami', 'pastrami']
finished_sandwiches = []

print("the deli has run out of pastrami")

while 'pastrami' in sandwich_orders :
    sandwich_orders.remove('pastrami')

while sandwich_orders :
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order} sandwich")
    finished_sandwiches.append(sandwich_order)

for finished_sandwiche in finished_sandwiches :
    print(finished_sandwiche)