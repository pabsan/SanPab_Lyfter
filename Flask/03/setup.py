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
    user1 = user_repo.create(name="John", last_name="Doe", status="active", birth_date="1990-01-01")
    #print(f"User created: {user1}")

    #updated_user = user_repo.update(user_id=2, name="Michelle", last_name="Smith", status="inactive", birth_date="1997-07-17")
    #print(f"Updated Name: {updated_user.name if updated_user else 'Failed'}")
    #deleted = user_repo.delete(user_id=2)
    #if deleted:
    #    print("User deleted successfully.")
    #else:
    #    print("User not found for deletion.")
except Exception as e:
    print("Connection failed:", e)