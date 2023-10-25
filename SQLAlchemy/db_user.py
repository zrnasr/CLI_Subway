from .database import db_get_obj, db_add_obj, db_run_query
from user.models import User, ticket_dict
from sqlalchemy import select, update, func
from menu.state import StateManager
from .database import Base

USERS = Base.metadata.tables['users']

def db_add_user(user):
    db_add_obj(user)

def db_get_user_by_password(username, password):
    query = select(User).where(User.username == username).where(User.password == password)
    if obj := db_get_obj(query):
        return obj.username
    
def db_get_user(username):
    query = select(User).where(User.username == username)
    if obj := db_get_obj(query):
        return obj.username
    
def db_ban_user(username):
    if db_get_user(username) == None:
        return
    query = update(USERS).values({"is_banned": 1}).where(USERS.c.username == username)
    db_run_query(query)
    return username

def db_add_chargeable_to_user(username):
    query = update(USERS).values({'ticket_dict': func.json_set(USERS.c.ticket_dict, "$.chargeable", USERS.c.ticket_dict["chargeable"] + 1)}).\
            where(USERS.c.username == username)
    db_run_query(query)                       
    

def db_add_disposable_to_user(username):
    query = update(USERS).values({'ticket_dict': func.json_set(USERS.c.ticket_dict, "$.disposable", USERS.c.ticket_dict["disposable"] + 1)}).\
            where(USERS.c.username == username)
    db_run_query(query) 