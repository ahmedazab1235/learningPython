def make_sandaweches(*troppings):
    """function to make sandawiches"""
    for tropping in troppings:
        print(f"- {tropping}")
    print('-----------------------')

make_sandaweches('frenshfries')
make_sandaweches('frenshfries', 'berger')
make_sandaweches('frenshfries', 'berger', 'katchab')