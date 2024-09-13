# Приклад використання SQLAlchemy для створення базового класу
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# Приклад використання PonyORM для створення базового класу
from pony.orm import Required, PrimaryKey, Database


db = Database(
    provider="postgres",
    user="username",
    password="password",
    host="localhost",
    database="dbname",
)


# Використовуємо той самий клас User для PonyORM
class UserPonyORM(db.Entity):
    id = PrimaryKey(int, auto=True)  # Для поніОРМ це НЕ обов'язкове поле
    name = Required(str)
    age = Required(int)


db.bind(provider="sqlite", filename=":memory:")
db.generate_mapping(create_tables=True)
