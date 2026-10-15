from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from Base import Invoice, InvoiceItem, Product


class InvoiceRepository:
    UPDATABLE_FIELDS = {
        "invoice_date"
    }
    READTABLE_FIELDS = {
        "id",
        "invoice_date",
        "amount"
    }

    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def create_invoice(self, invoice_date: str, user_id: int) -> Invoice:
        with self.session_factory() as session:
            invoice = Invoice(invoice_date = invoice_date, user_id = user_id)
            session.add(invoice)
            session.commit()
            return invoice

    def update(self, invoice_id: int, **kwargs) -> Invoice:
        with self.session_factory() as session:
            invoice = session.get(Invoice, invoice_id)
            if not invoice:
                raise ValueError(f"Invoice ID with {invoice_id} id does not exists.")
            for key, value in kwargs.items():
                if key not in self.UPDATABLE_FIELDS:
                    raise ValueError(f"Field {key} is not updatable in Invoice table.")
                setattr(invoice, key, value)

            session.commit()
            session.refresh(invoice)
            return invoice

    def delete(self, invoice_id: int) -> bool:
        with self.session_factory() as session:
            invoice = session.get(Invoice, invoice_id)
            if not invoice:
                raise ValueError(f"Invoice ID with {invoice_id} id does not exists.")
            session.delete(invoice)
            session.commit()
            return True

    def get_by_id(self, invoice_id: int) -> Invoice | None:
        with self.session_factory() as session:
            return session.get(Invoice, invoice_id)

    def get_all(self, **filter) -> list[Invoice]:
        with self.session_factory() as session:
            statement = select(Invoice)
            for key, value in filter.items():
                if key not in self.READTABLE_FIELDS:
                    raise ValueError(f"Field {key} is not in Invoice table.")
                statement = statement.where(getattr(Invoice, key) == value)
            return session.scalars(statement).all()

class InvoiceDetailRepository:
    UPDATABLE_FIELDS = {
        "invoice_id",
        "product_id",
        "quantity",
        "subtotal"
    }

    def __init__ (self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def valid_invoice(self, invoice_id) -> bool:
        with self.session_factory() as session:
            get_invoice = session.get(InvoiceItem, invoice_id)
            if get_invoice:
                return True
            else:
                return False

    def valid_line_id(self,line_id = int, invoice_id = int) -> bool:
        with self.session_factory() as session:
            get_line_id = session.get(InvoiceItem, {"invoice_id": invoice_id, "line_item_id":line_id})
            if get_line_id:
                return True
            else:
                return False

    def valid_product(self, product_id = int) -> bool:
        with self.session_factory() as sesssion:
            get_product = sesssion.get(Product, product_id)
            if get_product:
                return True
            else:
                return False

    def create_invoice_item(self, line_id: int, invoice_id: int, product_id: int, quantity: int):
        with self.session_factory() as session:
            if self.valid_invoice(invoice_id) and not self.valid_line_id(line_id,invoice_id) and self.valid_product(product_id):
                invoice_item = InvoiceItem(line_id,
                                           invoice_id,
                                           product_id,
                                           quantity)