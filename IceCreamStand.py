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


class IceCreamStand(Restaurant):
    """IceCreamStand that inherits from the Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        """resturant name and cuisine tpye and served castomers"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def displayflavors(self):
        for flavor in self.flavors:
            print(f"-- {flavor}")

my_icecreamstand = IceCreamStand('smozzy', 'ice cream')

my_icecreamstand.displayflavors()

my_icecreamstand = IceCreamStand('smozzy', 'ice cream', 'mango1', 'choklet')

my_icecreamstand.displayflavors()

