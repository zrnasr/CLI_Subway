from sqlalchemy import create_engine
from config import settings
from sqlalchemy_utils.functions import database_exists, create_database
from sqlalchemy.orm import declarative_base, Session

engine_url = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/subway"

Base = declarative_base()
engine = create_engine(engine_url)
if not database_exists(engine.url):
    create_database(engine.url)

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



