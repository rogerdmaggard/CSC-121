class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"""\nUser Information:\n
    First Name: {self.first_name.title()}\n
    Last Name: {self.last_name.title()}\n
    Age: {self.age}\n
    Email: {self.email}""")
        
    def greet_user(self):
        print(f"\nHello {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        print(f"\nLogin Attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"\nLogin attempts reset to {self.login_attempts}")

first_user = User('roger', 'maggard', '50', 'rogerdmaggard@students.abtech.edu')
first_user.describe_user()
first_user.greet_user()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.reset_login_attempts()


#second_user = User('abigail', 'maggard', '12', 'abigail@email.com')
#second_user.describe_user()
#second_user.greet_user()