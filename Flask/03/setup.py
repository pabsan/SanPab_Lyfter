from multiprocessing import connection

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from Base import Base, User, Address, Car
from UserRepository import UserRepository

DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

try:
    #create the tables in the database
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

    user_repo = UserRepository(SessionLocal)
    #user1 = user_repo.create(id=2, name="John", last_name="Doe", status="active", birth_date="1990-01-01")
    #print(f"User created: {user1}")

    updated_user = user_repo.update(user_id=2, name="Maria")
    print(f"Updated Name: {updated_user.name if updated_user else 'Failed'}")
except Exception as e:
    print("Connection failed:", e)