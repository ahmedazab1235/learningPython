class User :
    """gave a user information"""
    def __init__(self, first_name, last_name, age, job):
        """initializ firstname, lastname, age and job """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.login_attempts = 0

    def describe_user(self):
        """print user info"""
        print(f"fullname : {self.first_name} {self.last_name}")
        print(f"age : {self.age}")
        print(f"job : {self.job}")

    def greet_user(self):
        """print greetings to user"""

        print(f"Hallo, {self.first_name} {self.last_name}\n")

    def increment_login_attempts(self):
        """increments the value of login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets the value of login_attempts to 0."""
        self.login_attempts = 0

user_1 = User('Ahmed', 'Azab', 23, 'Engineer')
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)
