from sqlalchemy import create_engine
from Base import Base
from sqlalchemy.orm import sessionmaker

DB_URI = 'postgresql://postgres:admin123@localhost:5432/postgres'

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