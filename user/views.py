from .models import User
from SQLAlchemy.database import db_save_obj



def register(self):
    user = User(username="zahra", password="nasr")
    db_save_obj(user)


def login(self):
    pass


class BankAccount():

    def deposit(self, amount):
        BankAccount.__balance += amount

    def withdraw(self, amount):
        assert BankAccount.__balance >= amount, "Not Enough Balance!!"
        BankAccount.__balance -= amount 

    def get_balance(self):
        return BankAccount.__balance
    

