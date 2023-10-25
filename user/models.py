from sqlalchemy.orm import Mapped, mapped_column, relationship
from SQLAlchemy.database import Base, engine
from sqlalchemy import ForeignKey, Column, PickleType, JSON
from typing import Dict

ticket_dict = {"chargeable":0, "disposable":0}

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    is_banned: Mapped[bool] = mapped_column(default=False)
    ticket_dict = Column(JSON, default=ticket_dict)

    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    account: Mapped["BankAccount"] = relationship(back_populates="user")
    # ticket_id: Mapped[int] = mapped_column(ForeignKey("ticket.id"))
    # ticket: Mapped["Ticket"] = relationship(back_populates="users")


class BankAccount(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance : Mapped[float] = mapped_column(default= 365)

    user: Mapped["User"] = relationship(back_populates="account")

class Ticket(Base):
    __tablename__ = "ticket"

    id: Mapped[int] = mapped_column(primary_key=True)
    trip_fee: Mapped[float] = mapped_column(default= 50)
    year: Mapped[int] = mapped_column(default=2023)


Base.metadata.create_all(engine)