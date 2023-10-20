from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()
engine = create_engine("sqlite:///metro.sqlite3", echo=True)

def db_add_obj(obj):
    with Session(engine) as session:
        session.add(obj)
        session.commit()

def db_get_obj(query):
    with Session(engine) as session:
        for obj in session.scalars(query):
            print(obj)
            return obj
        print("Could not find any object.")

def db_run_query(query):
    with Session(engine) as session:
        session.execute(query)
        session.commit()



