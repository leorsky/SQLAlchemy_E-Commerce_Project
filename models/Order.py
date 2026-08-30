from sqlalchemy import ForeignKey
from e_commerce.database.connection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    status: Mapped[str] = mapped_column(default='pending')

    user: Mapped["User"] = relationship("User", back_populates="order")
    order_item: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="order")