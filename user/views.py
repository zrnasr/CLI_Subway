
class BankAccount:
    __balance = 500

    def deposit(self, amount):
        BankAccount.__balance += amount

    def withdraw(self, amount):
        assert BankAccount.__balance >= amount, "Not Enough Balance!!"
        BankAccount.__balance -= amount 

    def get_balance(self):
        return BankAccount.__balance
    

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.account = BankAccount

class Admin(User):
    pass
