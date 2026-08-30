from e_commerce.models.User import User
from e_commerce.models.Product import Product
from e_commerce.models.Category import Category
from e_commerce.models.Order import Order
from e_commerce.models.OrderItem import OrderItem
from e_commerce.database.connection import SessionLocal
from e_commerce.database.connection import Base, engine
from sqlalchemy import select


user1 = User(
    username="alex",
    email="alex@example.com",
)

user2 = User(
    username="mike",
    email="mike@example.com",
)

category1 = Category(
    name="Laptops",
)

category2 = Category(
    name="Smartphones",
)


product1 = Product(
    name="MacBook Air M3",
    price=1199.99,
    category=category1,
)

product2 = Product(
    name="Lenovo ThinkPad E16",
    price=899.50,
    category=category1,
)

product3 = Product(
    name="iPhone 16",
    price=999.00,
    category=category2,
)

order1 = Order(
    user=user1,
    status="pending",
)

order2 = Order(
    user=user2,
    status="completed",
)

item1 = OrderItem(
    order=order1,
    product=product1,
    quantity=1,
)

item2 = OrderItem(
    order=order1,
    product=product3,
    quantity=2,
)

item3 = OrderItem(
    order=order2,
    product=product2,
    quantity=1,
)

Base.metadata.create_all(engine)
