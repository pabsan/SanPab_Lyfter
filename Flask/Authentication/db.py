from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Numeric, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker
from Base import Base
from UserRepository import UserRepository

class DB_Manager:
    def __init__(self):
        DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
        engine = create_engine(DB_URI, echo=True)
        try:
            # Create the tables
            Base.metadata.create_all(engine)

            self.SessionLocal = sessionmaker(
                bind=engine,
                expire_on_commit=False
            )

        except Exception as e:
            print("Setup failed:", e)

    def insert_user(self, username: str, password: str):
       user_repo = UserRepository(self.SessionLocal)
       return user_repo.create(username,password)