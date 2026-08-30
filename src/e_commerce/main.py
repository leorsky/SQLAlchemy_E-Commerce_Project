from e_commerce.models.User import User
from e_commerce.models.Product import Product
from e_commerce.models.Category import Category
from e_commerce.models.Order import Order
from e_commerce.models.OrderItem import OrderItem
from e_commerce.models.Review import Review
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

review1 = Review(
    user=user2,
    product=product2,
    rating=5,
    comment="Excellent laptop, very fast and reliable!",
)

Base.metadata.create_all(engine)

with SessionLocal() as session:
    try:
        # session.add_all([
        #     user1,
        #     user2,
        #     category1,
        #     category2,
        #     product1,
        #     product2,
        #     product3,
        #     order1,
        #     order2,
        #     item1,
        #     item2,
        #     item3,
        # ])
        # session.commit()
        #
        # full_orm = [
        #     user1,
        #     user2,
        #     category1,
        #     category2,
        #     product1,
        #     product2,
        #     product3,
        #     order1,
        #     order2,
        #     item1,
        #     item2,
        #     item3,
        # ]
        #
        # for el in full_orm:
        #     session.refresh(el)

        statement1 = select(Product).where(Product.id == 1)
        result1 = session.execute(statement1)
        product_1 = result1.scalar_one_or_none()

        if product_1 is None:
            raise Exception(f'Продукт не найден.')
        else:
            print(f'{product_1.name} - {product_1.price}')

            for item in product_1.order_item:
                print(item.order.id, item.order.status)

        statement2 = select(Product)
        result2 = session.execute(statement2)
        products1 = result2.scalars()
        for el in products1:
            print(f'{el.name} - {el.price}\n')

        statement3 = select(Product).where(Product.price > 900)
        result3 = session.execute(statement3)
        products2 = result3.scalars().all()

        if not products2:
            raise Exception(f'Продукт не найден.')
        else:
            for el in products2:
                print(f'{el.name} - {el.price}\n')

        statement4 = select(Product).where(Product.name == "MacBook Air M3")
        result4 = session.execute(statement4)
        product_4 = result4.scalar_one_or_none()

        if product_4 is None:
            raise Exception(f'Продукт не найден.')
        else:
            product_4.price = 1299.99
            session.commit()
            session.refresh(product_4)

        statement5 = select(Product).where(Product.id == 3)
        result5 = session.execute(statement5)
        product_5 = result5.scalar_one_or_none()

        if product_5 is None:
            raise Exception(f'Продукт не найден.')
        else:
            session.delete(product_5)
            session.commit()

    except Exception as error:
        print(error)
        session.rollback()