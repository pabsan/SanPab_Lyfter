from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Numeric, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker
from Base import Base
from UserRepository import UserRepository
from ProductRepository import ProductRepository
from InvoiceRepository import InvoiceRepository
from InvoiceDetailRepository import InvoiceDetailRepository
from setup import SessionLocal

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

    def insert_user(self, username: str, password: str, user_type: str):
       user_repo = UserRepository(SessionLocal)
       return user_repo.create(username,password, user_type)

    def get_user(self, username: str, password:str):
        user_repo = UserRepository(SessionLocal)
        return user_repo.get_credentials(username,password)

    def get_user_by_id(self, user_id: int):
        user_repo = UserRepository(SessionLocal)
        return user_repo.get_by_id(user_id)

    def insert_product(self, name: str, price: float, entry_date: DateTime, quantity: Integer):
        product_repo = ProductRepository(SessionLocal)
        return product_repo.create(name, price, entry_date, quantity)

    def update_product(self, product_id: int, **kwargs):
        product_repo = ProductRepository(SessionLocal)
        return product_repo.update(product_id,**kwargs)

    def delete_product(self, product_id: int):
        product_repo = ProductRepository(SessionLocal)
        return product_repo.delete(product_id)

    def get_all_products(self, **filters):
        product_repo = ProductRepository(SessionLocal)
        return product_repo.get_all(**filters)

    def insert_invoice(self, invoice_date: str, user_id: int):
        invoice_repo = InvoiceRepository(SessionLocal)
        return invoice_repo.create_invoice(invoice_date, user_id)

    def update_invoice(self, invoice_id: int, **kwargs):
        invoice_repo = InvoiceRepository(SessionLocal)
        return invoice_repo.update(invoice_id,**kwargs)

    def delete_invoice(self, invoice_id: int):
        invoice_repo = InvoiceRepository(SessionLocal)
        return invoice_repo.delete(invoice_id)

    def get_invoice_by_id(self, invoice_id: int):
        invoice_repo = InvoiceRepository(SessionLocal)
        return invoice_repo.get_by_id(invoice_id)

    def get_all_invoices(self, **filters):
        invoice_repo = InvoiceRepository(SessionLocal)
        return invoice_repo.get_all(**filters)

    def get_invoice_by_userId(self, user_id: int):
        invo_repo = InvoiceRepository(SessionLocal)
        return invo_repo.get_by_user_id(user_id)

    def insert_invoice_detail(self, invoice_id: int, product_id: int, quantity: int):
        detail_repo = InvoiceDetailRepository(SessionLocal)
        return detail_repo.create(invoice_id,product_id,quantity)

    def update_invoice_detail(self, invoice_id: int, item:int):
        detail_repo = InvoiceDetailRepository(SessionLocal)
        return detail_repo.update(invoice_id,item)

    def replace_invoice_detail(self, invoice_id: int, items:list[dict]):
        detail_repo = InvoiceDetailRepository(SessionLocal)
        return detail_repo.replace_items(invoice_id,items)

    