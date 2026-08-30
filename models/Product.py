from sqlalchemy import Numeric, ForeignKey
from e_commerce.database.connection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[Decimal] = mapped_column(Numeric(10,2))
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))

    category: Mapped["Category"] = relationship("Category", back_populates="product")
    order_item: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="product", cascade="all, delete-orphan")