from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Numeric, DateTime, ForeignKey
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
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    items: Mapped[list["InvoiceItem"]] = relationship(
        back_populates="invoice", cascade="all, delete-orphan"
    )

    @property
    def total_amount(self) -> float:
        return sum(item.calculate_subtotal for item in self.items)

    def __repr__(self) -> str:
        return f""" Invoice (id={self.id!r}),
        Invoice Date = {self.invoice_date},
        Amount = {self.total_amount}"""

class InvoiceItem(Base):
    __tablename__ = "invoice_items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(Integer)

    invoice: Mapped["Invoice"] = relationship(back_populates="items")
    product: Mapped["Product"] = relationship()

    @property
    def calculate_subtotal(self) -> float:
            if self.product and self.quantity:
                return self.quantity * self.product.price
            return 0.00

    def __repr__(self) -> str:
        return f""" Id (id={self.id!r}),
        Invoice ID = {self.invoice_id},
        Product ID = {self.product_id},
        Quantity = {self.quantity},
        Subtotal = {self.calculate_subtotal})"""
