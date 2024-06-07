from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
DATABASE_URL = "postgresql://postgres:postgres@localhost/my_db"
# DATABASE_URL = "postgresql://username:password@localhost/database_name"


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)


try:
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Відповідає INSERT INTO users (username, email) VALUES ('John', 'users@email');
    new_user = User(username='John', email='users@email')
    session.add(new_user)
    session.commit()

    # Відповідає UPDATE users SET email=jogn@email.com WHERE name='John';
    user = session.query(User).filter_by(username='John').first()
    print(user.username)
    user.email = 'john@email.com'
    session.commit()

    # Відповідає DELETE FROM users WHERE name='John';
    session.delete(user)
    session.commit()

    # Вибірка всіх користувачів
    all_users = session.query(User).all()
    # SQL аналог: SELECT * FROM users;

    # Фільтрація за умовою
    john = session.query(User).filter_by(username='John').first()
    # SQL аналог: SELECT * FROM users WHERE username = 'John' LIMIT 1;

    # Сортування
    sorted_users = session.query(User).order_by(User.username.desc()).all()
    # SQL аналог: SELECT * FROM users ORDER BY username DESC;

except Exception as e:
    print('Error', e)

