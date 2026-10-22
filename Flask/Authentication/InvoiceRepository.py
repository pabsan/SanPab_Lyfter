from sqlalchemy.orm import sessionmaker, selectinload
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

    def get_by_user_id(self, user_id: int, **filter) -> list[Invoice]:
        with self.session_factory() as session:
            statement = select(Invoice).where(Invoice.user_id == user_id)
            for key, value in filter.items():
                if key not in self.READTABLE_FIELDS:
                    raise ValueError(f"Field {key} is not in Invoice table.")
                statement = statement.where(getattr(Invoice, key) == value)
            return session.scalars(statement).all()

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
        "product_id",
        "quantity"
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

    def valid_product(self, product_id = int) -> bool:
        with self.session_factory() as sesssion:
            get_product = sesssion.get(Product, product_id)
            if get_product:
                return True
            else:
                return False

    def create(self, invoice_id: int, product_id: int, quantity: int):
        with self.session_factory() as session:
            if self.valid_invoice(invoice_id) and self.valid_product(product_id):
                invoice_item = InvoiceItem(invoice_id,
                                           product_id,
                                           quantity)
                session.add(invoice_item)
                session.commit()
                return invoice_item
            else:
                return None

    def update(self, invoice_id: int, item_id: int, **kargs) -> Invoice | None:
        with self.session_factory() as session:
            item = session.get(InvoiceItem, invoice_id, item_id)

            if not item:
                raise ValueError("Item not found")

            for key, value in kargs.items():
                if key is not self.UPDATABLE_FIELDS:
                    raise ValueError("Fiel {key} is not updatable")

                if key == "quantity":
                    if not isinstance(value, int) or value <= 0:
                        raise ValueError("Quantity must be positive integer")
                if key == "product_id":
                    if not session.get(Product,value):
                        raise ValueError("Product Not Found")

                setattr(item, key,value)

            session.commit()
            session.refresh(item)

            return item

    def replace_items(self, invoice_id: int, items:list[dict]) -> Invoice:
        with self.session_factory() as session:
            invoice = session.get(Invoice, invoice_id)

            if not invoice:
                raise ValueError("Invoice Not Found")

            #validate and consolidate products
            quantities = {}
            for item in items:
                if "product_id" not in item or "quantity" not in item:
                    raise ValueError("Each item must have product id and quantity")

                product_id = item["product_id"]
                quantity = item["quantity"]

                if (not session.get(Product,product_id)):
                    raise ValueError("Product not found")

                if (not isinstance(quantity, int) or quantity <= 0):
                    raise ValueError("Quantity must be integer positive number")

                quantities [product_id] = (quantities.get(product_id,0) + quantity)

            invoice.items.clear()

            for product_id, quantity in quantities.items():
                invoice.items.append(
                    InvoiceItem(product_id = product_id, quantity =quantity)
                )

            session.flush()
            session.commit()

            statement = (select(Invoice)
                         .options(
                             selectinload(Invoice.items)
                             .selectinload(InvoiceItem.product)
                         )
                         .where(Invoice.id == invoice_id)
                         )
            return session.scalar(statement)
                    

