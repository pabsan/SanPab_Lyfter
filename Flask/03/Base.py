from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy import create_engine, func
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from datetime import date, datetime
from typing import List
from typing import Optional


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(50))
    last_name:Mapped[str] = mapped_column(String(100))
    status:Mapped[str] = mapped_column(String(20))
    birth_date:Mapped[date] = mapped_column()

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    cars: Mapped[Optional[List["Car"]]] = relationship(
        back_populates="user"
    )

    def __repr__(self) -> str:
        return f"""User (id={self.id!r}, name={self.name!r}, last_name={self.last_name!r}, 
        status={self.status!r}, birth_date={self.birth_date!r}, created_at={self.created_at!r}, 
        updated_at={self.updated_at!r})"""

class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    street: Mapped[str] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(50))
    state: Mapped[str] = mapped_column(String(50))
    zip_code: Mapped[str] = mapped_column(String(10))

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"""Address (id={self.id!r}, user_id={self.user_id!r}, street={self.street!r}, 
        city={self.city!r}, state={self.state!r}, zip_code={self.zip_code!r}, 
        created_at={self.created_at!r}, updated_at={self.updated_at!r})"""

class Car(Base):
    __tablename__ = "Cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )
    brand: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(50))
    year: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(20))

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    user: Mapped[Optional["User"]] = relationship(back_populates="cars")

    def __repr__(self) -> str:
        return f"""Car (id={self.id!r}, user_id={self.user_id!r}, brand={self.brand!r}, 
        model={self.model!r}, year={self.year!r}, status={self.status!r}, 
        created_at={self.created_at!r}, updated_at={self.updated_at!r})"""