import json
import pickle
import glob
import os
from src import clear

user_path = "user/"

def show_menu(dictionary):
    print(json.dumps(dictionary, indent = 4))

def save_user(obj):
    if not os.path.exists(user_path):
        os.makedirs(user_path)
    with open(f"{user_path}{obj.id}.pickle", 'wb') as user:
        pickle.dump(obj, user)

def get_unique_id(user_id):
    with open(f"{user_path}{user_id}.pickle", 'rb') as user:
        return pickle.load(user)

def get_unique_id_from_username():
    object_content = []
    for file in glob.glob(f"{user_path}*.pickle"):
        with open(file, 'rb') as fd:
            while True:
                try:
                    content = pickle.load(fd)
                    object_content.append(content)
                except EOFError:
                    break

    name = input('Enter username: ')
    password = input('Enter password: ')
    if object_content == []:
        input("Please register first ...")
    for user in object_content:
        if user.username == name:
            if user.password == password:
                print(f'Your id is:\n{user.id}')
                input('Done. Login again with your id ...')
                break
            else:
                input("Wrong Password, Click any key to continue ...")
        else:
            input("Wrong username, Click any key to continue ...")
            break

def pickle_tickets(ticket_obj):
    ticket_path = "ticket/"
    if not os.path.exists(ticket_path):
        os.makedirs(ticket_path)
    with open(f"{ticket_path}{ticket_obj.ticket_id}.ticket.pickle" , 'wb') as ticket:
        pickle.dump(ticket_obj, ticket)


