from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Numeric, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker

#metadata_obj = MetaData()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[String] = mapped_column(String(30))
    password: Mapped[String] = mapped_column(String)

    def __repr__(self) -> str:
        return f""" User (id ={self.id!r}), username={self.username}"""

class products(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String(50))
    price: Mapped[Numeric] = mapped_column(Numeric(10,2))
    entry_date: Mapped[DateTime] = mapped_column(DateTime)
    quatity: Mapped[int] = mapped_column(Integer)
