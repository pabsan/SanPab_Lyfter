import datetime

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Numeric, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import numeric 


from sqlalchemy import insert, select

metadata_obj = MetaData()

class Base(DeclarativeBase):
    pass

class users(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[String] = mapped_column(String(30))
    password: Mapped[String] = mapped_column(String) 

class products(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String(50))
    price: Mapped[Numeric] = mapped_column(Numeric(10,2))
    entry_date: Mapped[DateTime] = mapped_column(DateTime)
    quatity: Mapped[int] = mapped_column(Integer)

class DB_Manager:
    def __init__(self):
        self.engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
        metadata_obj.create_all(self.engine)

    def insert_user(self, username, password):
        qry = insert(user_table).returning(user_table.c.id).values(username=username,password=password)
        with self.engine.connect() as conn:
            result = conn.execute(qry)
            conn.commit()
        return result.all()[0]

    def get_user(self, username,password):
        qry = select(user_table).where(user_table.c.username == username).where(user_table.c.password == password)
        with self.engine.connect() as conn:
            result = conn.execute(qry)
            users = result.all()

            if len(users) == 0:
                return None
            else:
                return users[0]

    def get_user_by_id(self, id):
        qry = select(user_table).where(user_table.c.id == id)
        with self.engine.connect() as conn:
            result = conn.execute(qry)
            users = result.all()
            if len(users) == 0:
                return None
            else:
                return users[0]
