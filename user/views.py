from SQLAlchemy.db_user import db_get_user, db_add_user, db_ban_user
from .models import User
from menu.state import StateManager

def register(route):
    try:
        username = input("Choose a username please: ") #add regex
        password = input("Choose a password please: ")
        user = User(username=username, password=password)
        db_add_user(user)
        print("Successfuly Registered!")
    except:
        print("Error in Registering! Please Try again!")


def login(route):
    try:
        username = input("Enter your username please: ") #add regex
        password = input("Enter your password please: ")
        user = db_get_user(username, password)
        if user:
            StateManager.set_user(user)
            print(f"Hello {user}!")
        else:
            print("There is no user with this username. Please register first!")
    except:
        print("Error in Logging in! Try again!")

def logout(route):
    StateManager.logout()
    print("Logged out!")

def ban_user(route):
    user = input("Enter the username of the person that is is need to be banned: ")
    db_ban_user(user)

# class BankAccount():
#     def deposit(self, amount):
#         BankAccount.__balance += amount

#     def withdraw(self, amount):
#         assert BankAccount.__balance >= amount, "Not Enough Balance!!"
#         BankAccount.__balance -= amount 

#     def get_balance(self):
#         return BankAccount.__balance
