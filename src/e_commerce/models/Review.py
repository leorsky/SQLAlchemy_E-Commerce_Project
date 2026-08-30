from datetime import datetime
from e_commerce.database.connection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint, ForeignKey


class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int]
    comment: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    test1: Mapped[str] = mapped_column(default='test1')

    user: Mapped["User"] = relationship("User", back_populates="reviews")
    product: Mapped["Product"] = relationship("Product", back_populates="reviews")


    __table_args__ = (
        CheckConstraint('rating>=1 AND rating<=5'),
    )