from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

class Base(declarative_base):
    pass

engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add_all()
#     session.commit()