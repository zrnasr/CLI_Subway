from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()
engine = create_engine("sqlite:///metro.sqlite3", echo=True)


def db_save_obj(obj):
    with Session(engine) as session:
        session.add(obj)
        session.commit()

