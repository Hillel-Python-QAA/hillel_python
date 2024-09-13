from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# З'єднання з базою даних PostgreSQL (замініть дані на ваші)
DATABASE_URL = "postgresql://postgres:postgres@localhost/my_db"
engine = create_engine(DATABASE_URL)

# Створення базового класу для визначення моделей даних
Base = declarative_base()


# Визначення моделі даних (таблиці) за допомогою класу
class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)


# Створення таблиці у базі даних
Base.metadata.create_all(engine)

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Початок транзакції
    session.begin()

    # Додавання нового продукту
    new_product = Product(name="Laptop", price=1000)
    session.add(new_product)

    # Збільшення ціни для всіх продуктів на 10%
    session.query(Product).update({Product.price: Product.price * 1.1})

    # Збільшення ціни для конкретного продукту на 5%
    product = session.query(Product).filter_by(name="Laptop").first()
    product.price *= 1.05

    # Підтвердження транзакції
    session.commit()
except:
    # Скасування транзакції в разі виникнення помилки
    session.rollback()
    raise
finally:
    # Закриття сесії
    session.close()
