class Restaurant:
    """class of resturant"""
    def __init__(self, restaurant_name, cuisine_type):
        """resturant name and cuisine tpye"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """method called describe_restaurant() that prints these two pieces of information"""
        print(f"restaurant name is {self.restaurant_name}")
        print(f"cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """prints a message indicating that the restaurant is open."""
        print("restaurant is open")

restaurant_1 = Restaurant('Fwaz', 'Shawerma')
restaurant_2 = Restaurant('El bet elsory', 'wagabat')
restaurant_3 = Restaurant('mac', 'berger')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()