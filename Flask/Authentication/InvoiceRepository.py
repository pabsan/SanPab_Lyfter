from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from Base import Invoice

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

    def create_invoice(self, invoice_date: str) -> Invoice:
        with self.session_factory() as session:
            invoice = Invoice(invoice_date = invoice_date)
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
