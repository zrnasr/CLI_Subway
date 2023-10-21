from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey
from SQLAlchemy.database import Base, engine

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    username: Mapped[str]
    password: Mapped[str]
    is_banned: Mapped[bool] = mapped_column(default=False)
    account = relationship("BankAccount")


class BankAccount(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance : Mapped[float] = mapped_column(default= 100)

class Ticket(Base):
    __tablename__ = "ticket"

    id: Mapped[int] = mapped_column(primary_key=True)
    trip_fee: Mapped[float] = mapped_column(default= 50)

Base.metadata.create_all(engine)