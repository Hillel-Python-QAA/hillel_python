from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.orm import sessionmaker, declarative_base

# З'єднання з базою даних PostgreSQL (замініть дані на ваші)
DATABASE_URL = "postgresql://postgres:postgres@localhost/my_db"
engine = create_engine(DATABASE_URL)

# Створення базового класу для визначення моделей даних
Base = declarative_base()


# Визначення моделі даних (таблиці) за допомогою класу
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# Створення таблиці у базі даних
Base.metadata.create_all(engine)

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

# Додавання користувачів до бази даних
session.add_all([
    User(name='John', age=30),
    User(name='Alice', age=25),
    User(name='Bob', age=35),
])
session.commit()
# SQL аналог:
# INSERT INTO users (name, age) VALUES ('John', 30), ('Alice', 25), ('Bob', 35);

# Використання виразів для складного запиту: обчислення середнього віку користувачів
average_age = session.query(func.avg(User.age)).scalar()
print("Середній вік користувачів:", average_age)
# SQL аналог: SELECT AVG(age) FROM users;

# Використання виразів для складного запиту: підрахунок кількості користувачів
user_count = session.query(func.count(User.id)).scalar()
print("Кількість користувачів:", user_count)
# SQL аналог: SELECT COUNT(id) FROM users;

# Закриття сесії
session.close()
