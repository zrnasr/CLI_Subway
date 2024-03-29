from .database import Base, db_get_obj, db_run_query
from sqlalchemy import select, update
from .models import BankAccount, User

ACCOUNT = Base.metadata.tables['account']

def db_get_balance(username):
    query = select(BankAccount).join(User).where(User.username == username)
    if obj := db_get_obj(query):
        return obj.balance
    
def db_withdraw(username, amount):
    query = update(ACCOUNT).values({"balance": ACCOUNT.c.balance - amount}).where(ACCOUNT.c.id == select(BankAccount.id).join(User).where(User.username == username).as_scalar())
    db_run_query(query)

def db_deposit(username, amount):
    query = update(ACCOUNT).values({"balance": ACCOUNT.c.balance + amount}).where(ACCOUNT.c.id == select(BankAccount.id).join(User).where(User.username == username).as_scalar())
    db_run_query(query)
