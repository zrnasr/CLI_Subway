from .database import Base, db_get_obj, db_run_query
from sqlalchemy import select, update
from menu.state import StateManager
from user.models import BankAccount, User

ACCOUNT = Base.metadata.tables['account']
USERS = Base.metadata.tables['users']

def db_get_balance():
    username = StateManager.get_user()
    query = select(BankAccount).join(User).where(User.username == username)
    if obj := db_get_obj(query):
        return obj.balance
    
def db_withdraw(username, amount):
    query = update(ACCOUNT).values({"balance": ACCOUNT.c.balance - 50}).where(select(BankAccount.id).join(User).where(User.username == username).as_scalar())
    db_run_query(query)
