import uuid
from src import BankAccount
import re
import os
import pickle

class User:
    def __init__(self, username, password):
        self.username = username
        self._validate_password(password)
        self.__password = password
        self.account = BankAccount(title = "Main_Account", balance = 10)
        self.ticket_list = []
        self.__id = uuid.uuid1()
        self.banned_user = False

    #getter id
    @property
    def id(self):
        return self.__id

    #getter password
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, newpass):
        self._validate_password(newpass)
        self.__password = newpass

    @staticmethod
    def _validate_password(password):
        assert re.fullmatch(r'^(?=.*\d)(?=.*[a-z])(?=.*[a-zA-Z]).{8,}$', password), ("Invalid password. should contains a-z, 0-9, at least 8 chars, ..")


    def find_user(self, filename, search_path):
        result = []
        for root, dirname, files in os.walk(search_path):
            if filename in files:
                result.append(os.path.join(root, filename))
        with open(f'{result[0]}', 'rb') as f:
            user = pickle.load(f)
        return user

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def show_balance(self, name):
        return self.account.calculate_balance(name)

    def buy_ticket(self, ticket):
        self.ticket_list.append(ticket)


    def charge_chargeble_ticket(self, number, amount):
        self.ticket_list[number - 1].charge_ticket(amount)

    def show_ticket_list(self):
        for ticket in (self.ticket_list):
            yield ticket


class SuperUser(User):

    def __init__(self, username, password):
        super().__init__(username, password)
        self.__id = uuid.uuid1()


    def set_blacklist(self, user : User):
        user.banned_user = True
