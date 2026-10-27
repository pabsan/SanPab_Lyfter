from sqlalchemy.orm import sessionmaker, selectinload
from sqlalchemy import select
from Base import Invoice, InvoiceItem, Product
from ProductRepository import ProductRepository
from InvoiceRepository import InvoiceRepository

class InvoiceDetailRepository:
    UPDATABLE_FIELDS = {
        "product_id",
        "quantity"
    }

    def __init__ (self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def valid_invoice(self, invoice_id) -> bool:
        with self.session_factory() as session:
            invoice_repo = InvoiceRepository(session)
            get_invoice = invoice_repo.get_by_id (invoice_id)
            if get_invoice:
                return True
            else:
                return False

    def valid_product(self, product_id = int) -> bool:
        with self.session_factory() as sesssion:
            product_repo = ProductRepository(sesssion)
            get_product = product_repo(product_id)
            if get_product:
                return True
            else:
                return False

    def get_quantities(self, invoice_id: int, items:list[dict]):
        quantities = {}
        for item in items:
            if "product_id" not in item or "quantity" not in item:
                raise ValueError("Each item must have a product id and quantity")
            product_id = item["product_id "]
            quantity = item["quantity"]

            if not self.valid_product(product_id):
                raise ValueError(f"Product with id {product_id} not found")

            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Quantity must be a positive integer")

            quantities[product_id] = quantities.get(product_id, 0) + quantity
        return quantities


    def create(self, invoice_id: int, items: list[dict]) -> list[InvoiceItem] | None:
        with self.session_factory() as session:
            if self.valid_invoice(invoice_id):
                quantities = self.get_quantities(invoice_id,items)
                invoice_items = []
                for product_id, quantity in quantities.items():
                    invoice_item = InvoiceItem(invoice_id, product_id, quantity)
                    session.add(invoice_item)
                    invoice_items.append(invoice_item)

                session.commit()
                return invoice_items
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
            quantities = self.get_quantities(invoice_id, items)

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
                    

