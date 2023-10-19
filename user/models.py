from sqlalchemy.orm import Mapped, mapped_column, relationship
from SQLAlchemy.database import Base, engine
from sqlalchemy import ForeignKey

class User(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"), nullable= True)
    username: Mapped[str]
    password: Mapped[str]
    account = relationship("BankAccount")


class BankAccount(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance : Mapped[float] = mapped_column(default= 500)


Base.metadata.create_all(engine)