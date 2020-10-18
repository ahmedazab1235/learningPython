sandwich_orders = ['derger', 'egg', 'frenshfries']
finished_sandwiches = []

while sandwich_orders :
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order} sandwich")
    finished_sandwiches.append(sandwich_order)

for finished_sandwiche in finished_sandwiches :
    print(finished_sandwiche)