from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from SQLAlchemy.database import Base
from .user import User


class BankAccount(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    __balance : Mapped[float]
    user: Mapped["User"] = relationship(back_populates="account")



