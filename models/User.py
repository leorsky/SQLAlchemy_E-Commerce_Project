from e_commerce.database.connection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)

    order: Mapped[list["Order"]] = relationship("Order", back_populates="user")
