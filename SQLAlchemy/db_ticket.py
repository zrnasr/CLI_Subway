from .db_user import db_add_chargeable_to_user, db_add_disposable_to_user
from .db_account import db_get_balance, db_withdraw
from menu.state import StateManager
from user.models import Ticket
from .database import db_get_obj
from sqlalchemy import select

current_year = 2023

def db_buy_chargeable_ticket():
    fee = get_trip_fee()
    assert db_get_balance() >= fee, print("Not Enough Money to Buy Chargeable Ticket!")
    username = StateManager.get_user()
    db_withdraw(username)
    db_add_chargeable_to_user(username)
        

def db_buy_disposable_ticket():
    fee = get_trip_fee()
    assert db_get_balance() >= fee, print("Not Enough Money to Buy Disposable Ticket!")
    username = StateManager.get_user()
    db_withdraw(username)
    db_add_disposable_to_user(username)
        
def db_charge_chargeable_ticket(amount):
    assert db_get_balance() >= amount, print("Not Enough Money to charge Chargeable Ticket!")
    username = StateManager.get_user()
    db_withdraw(username)
    ...

def get_trip_fee():
    query = select(Ticket.trip_fee).where(Ticket.year == current_year)
    if obj := db_get_obj(query):
        return obj.trip_fee