from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Base import Base, User, Address, Car
from UserRepository import UserRepository
from CarRepository import CarRepository
from AddressRepository import AddressRepository


DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'

engine = create_engine(DB_URI, echo=True)

try:
    # Create the tables
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(
        bind=engine,
        expire_on_commit=False
    )

except Exception as e:
    print("Setup failed:", e)