from .database import Base, db_get_obj
from sqlalchemy import select
from menu.state import StateManager
from user.models import BankAccount, User

def db_get_balance():
    username = StateManager.get_user()
    query = select(BankAccount).join(User).where(User.username == username)
    if obj := db_get_obj(query):
        return obj.balance