from sqlalchemy.orm import Mapped, mapped_column, relationship
from SQLAlchemy.database import Base

class User(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    __password: Mapped[str]
    account: Mapped["BankAccount"] = relationship(back_populates= "user")


class BankAccount(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    __balance : Mapped[float]
    user: Mapped["User"] = relationship(back_populates="account")


    


