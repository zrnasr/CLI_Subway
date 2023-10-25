from menu.routes import *
from SQLAlchemy.db_ticket import db_add_ticket

def main():
    db_add_ticket()
    router()

if __name__ == '__main__':
    main()