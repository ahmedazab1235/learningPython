class User :
    """gave a user information"""
    def __init__(self, first_name, last_name, age, job):
        """initializ firstname, lastname, age and job """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

    def describe_user(self):
        """print user info"""
        print(f"fullname : {self.first_name} {self.last_name}")
        print(f"age : {self.age}")
        print(f"job : {self.job}")

    def greet_user(self):
        """print greetings to user"""

        print(f"Hallo, {self.first_name} {self.last_name}\n")

user_1 = User('Ahmed', 'Azab', 23, 'Engineer')
user_2 = User('mohamed', 'mgaqry', 23, 'Capten')
user_3 = User('alaa', 'mamdouh', 23, 'teacher')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
