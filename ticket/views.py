from SQLAlchemy.db_ticket import db_buy_chargeable_ticket, db_buy_disposable_ticket, db_charge_chargeable_ticket
from SQLAlchemy.db_user import db_has_chargeable_ticket

def buy_chargeable(route):
    try:
        db_buy_chargeable_ticket()
        print("Successfuly bought a chargeable ticket!")
    except Exception as e:
        print("Could not buy chargeable ticket! ", e)


def buy_disposable(route):
    try:
        db_buy_disposable_ticket()
        print("Successfuly bought a disposable ticket!")
    except Exception as e:
        print("Could not buy disposable ticket! ", e)


def charge_chargeable_ticket(route):
    try:
        assert db_has_chargeable_ticket(), "There is no Chargeable ticket to charge! Please buy one first."
        amount = int(input("How much do you want to charge your ticket? "))
        db_charge_chargeable_ticket(amount)
        print("Successfuly charged the Chargeable ticket!")
    except Exception as e:
        print("Could not charge the Chargeable ticket! ", e)