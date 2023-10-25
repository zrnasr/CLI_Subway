from SQLAlchemy.db_user import db_get_user_by_password, db_add_user, db_ban_user
from SQLAlchemy.db_account import db_get_balance
from SQLAlchemy.db_ticket import db_buy_chargeable_ticket, db_buy_disposable_ticket, db_charge_chargeable_ticket
from .models import User, BankAccount
from menu.state import StateManager

def register(route):
    try:
        username = input("Choose a username please: ") #add regex
        password = input("Choose a password please: ")
        account = BankAccount()
        user = User(username=username, password=password, account = account)
        db_add_user(user)
        print("Successfuly Registered!")
    except:
        print("Error in Registering! Please Try again!")

def login(route):
    try:
        username = input("Enter your username please: ") #add regex
        password = input("Enter your password please: ")
        user = db_get_user_by_password(username, password)
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
    try:
        user = input("Enter the username of the person that is is need to be banned: ")
        if db_ban_user(user):
            print(f"User {user} is successfuly banned from this application.")
        else:
            print(f"User {user} not found!")
    except Exception as e:
        input("Error!! Something is wrong!", e)

def balance(route):
    try:
        balance = db_get_balance()
        print(f"Your balance is {balance}.")
    except Exception as e:
        input("Error!! Something is wrong!", e)
    
def chargeable(route):
    try:
        db_buy_chargeable_ticket()
        print("Successfuly bought a chargeable ticket!")
    except Exception as e:
        print("Could not buy chargeable ticket! ", e)


def disposable(route):
    try:
        db_buy_disposable_ticket()
    except Exception as e:
        print("Could not buy disposable ticket! ", e)


def charge_chargeable_ticket(route):
    try:
        amount = input(int("How much do you want to charge your ticket? "))
        db_charge_chargeable_ticket(amount)
    except Exception as e:
        ...
