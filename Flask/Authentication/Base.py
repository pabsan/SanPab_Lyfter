from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Numeric, DateTime, ForeignKey, Decimal
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

#metadata_obj = MetaData()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[String] = mapped_column(String(30))
    password: Mapped[String] = mapped_column(String)
    user_type: Mapped[String] = mapped_column(String(30), default="user")

    def __repr__(self) -> str:
        return f""" User (id ={self.id!r}), username={self.username}, user_type={self.user_type}"""

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String(50))
    price: Mapped[Numeric] = mapped_column(Numeric(10,2))
    entry_date: Mapped[DateTime] = mapped_column(DateTime)
    quantity: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f""" Product (id={self.id!r}),
        Name = {self.name},
        price={self.price},
        entry_date={self.entry_date},
        quantity={self.quantity}"""

class Invoice(Base):
    __tablename__ = "invoices"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    invoice_date: Mapped[DateTime] = mapped_column(DateTime)
    amount: Mapped[float] = mapped_column(float)

    items: Mapped[list["InvoiceItem"]] = relationship(
        back_populates="invoice", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f""" Invoice (id={self.id!r}),
        Invoice Date = {self.invoice_date},
        Amount = {self.amount}"""

class InvoiceItem(Base):
    __tablename__ = "invoice_items"
    line_item_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    subtotal: Mapped[Decimal] = mapped_column(Numeric(10,2), default=0.00)

    invoice: Mapped["Invoice"] = relationship(back_populates="items")
    product: Mapped["Product"] = relationship()


    def __repr__(self) -> str:
        return f""" InvoiceItem (id={self.id!r}),
        Invoice ID = {self.invoice_id},
        Product ID = {self.product_id},
        Quantity = {self.quantity},
        Subtotal = {self.subtotal}"""
