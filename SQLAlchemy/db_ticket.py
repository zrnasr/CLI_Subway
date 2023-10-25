from .db_user import db_add_chargeable_to_user, db_add_disposable_to_user
from .db_account import db_get_balance, db_withdraw
from core.state import StateManager
from .models import Ticket
from .database import db_get_obj, db_add_obj
from sqlalchemy import select

current_year = 2023

def db_add_ticket():
    ticket = Ticket()
    db_add_obj(ticket)

def db_buy_chargeable_ticket():
    fee = get_trip_fee()
    username = StateManager.get_user()
    assert db_get_balance(username) >= fee, "Not Enough Money to Buy Chargeable Ticket!"
    db_withdraw(username, fee)
    db_add_chargeable_to_user(username)

def db_buy_disposable_ticket():
    fee = get_trip_fee()
    username = StateManager.get_user()
    assert db_get_balance(username) >= fee, "Not Enough Money to Buy Disposable Ticket!"
    db_withdraw(username, fee)
    db_add_disposable_to_user(username)
        
def db_charge_chargeable_ticket(amount):
    username = StateManager.get_user()
    assert db_get_balance(username) >= amount, "Not Enough Money to charge Chargeable Ticket!"
    db_withdraw(username, amount)    

def get_trip_fee():
    query = select(Ticket).where(Ticket.year == current_year)
    if obj := db_get_obj(query):
        return obj.trip_fee