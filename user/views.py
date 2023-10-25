from SQLAlchemy.db_user import db_get_user_by_password, db_add_user, db_ban_user, db_check_banned_user
from SQLAlchemy.db_account import db_get_balance, db_deposit
from core.utils import validate_password
from SQLAlchemy.models import User, BankAccount
from core.state import StateManager

def register(route):
    try:
        username = input("Choose a username please: ")
        assert username, "Please fill username field!"
        password = input("Choose a password please: ")
        validate_password(password)
        account = BankAccount()
        user = User(username=username, password=password, account = account)
        db_add_user(user)
        print("Successfuly Registered!")
    except Exception as e:
        print("Error! ", e)

def login(route):
    try:
        username = input("Enter your username please: ")
        password = input("Enter your password please: ")
        obj = db_get_user_by_password(username, password)
        if obj:
            assert db_check_banned_user(obj) == False, "You are in the blacklist! Can NOT Login!"
            StateManager.set_user(username)
            print(f"Hello {username}!")
        else:
            print("There is no user with this username. Please register first!")
    except Exception as e:
        print("Error! ", e)

def logout(route):
    StateManager.logout()
    print("Logged out!")

def ban_user(route):
    try:
        user = input("Enter the username of the person that is is need to be banned: ")
        if db_ban_user(user):
            print(f"User {user} is successfuly banned from this application.")
        else:
            print(f"User {user} not found!")
    except Exception as e:
        print("Error!! Something is wrong!", e)

def balance(route):
    try:
        user = StateManager.get_user()
        balance = db_get_balance(user)
        print(f"Your balance is {balance}.")
    except Exception as e:
        print("Error!! Something is wrong!", e)

def deposit(route):
    try:
        user = StateManager.get_user()
        amount = int(input("How much do you want to deposit? "))
        db_deposit(user, amount)
        print(f"Operation is Successful!")
    except Exception as e:
        print("Error!! Something is wrong!", e)
    

