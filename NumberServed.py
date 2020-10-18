class Restaurant:
    """class of resturant"""
    def __init__(self, restaurant_name, cuisine_type):
        """resturant name and cuisine tpye"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """method called describe_restaurant() that prints these two pieces of information"""
        print(f"restaurant name is {self.restaurant_name}")
        print(f"cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """prints a message indicating that the restaurant is open."""
        print("restaurant is open")
    def set_number_served(self, nuserved):
        self.number_served = nuserved

    def increment_number_served(self, increase):
        self.number_served += increase

restaurant_1 = Restaurant('fwaz', 'shawerma')

print(restaurant_1.number_served)

restaurant_1.number_served = 9

print(restaurant_1.number_served)

restaurant_1.set_number_served(77)

print(restaurant_1.number_served)

restaurant_1.increment_number_served(7)

print(restaurant_1.number_served)