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

my_restaurant = Restaurant('fwaz el sory', 'shawerma')

print(f"restaurant name is {my_restaurant.restaurant_name} and we offer {my_restaurant.cuisine_type}")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()




