from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from Base import Product

class ProductRepository:
    UPDATABLE_FIELDS = {
        "name",
        "price",
        "entry_date",
        "quantity"
    }

    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def create(self, name: str, price: float, entry_date: str, quantity: int) -> Product:
        with self.session_factory() as session:
            product = Product(name = name, price = price, entry_date = entry_date, quantity= quantity)
            session.add(product)
            session.commit()
            return product

    def update(self, product_id: int, **kwargs) -> Product:
        with self.session_factory() as session:
            product = session.get(Product, product_id)
            if not product:
                raise ValueError(f"Product ID with {product_id} id does not exists")
            for key, value in kwargs.items():
                if key not in self.UPDATABLE_FIELDS:
                    raise ValueError(f"Field '{key} is not updatable in Products table'")
                setattr(product, key, value)

            session.commit()
            session.refresh(product)
            return product

    def delete(self, product_id: int) -> bool:
        with self.session_factory() as session:
            product = session.get(Product, product_id)
            if not product:
                return False

            session.delete(product)
            session.commit()
            return True

    def get_by_id(self, product_id: int) -> Product | None:
        with self.session_factory() as session:
            return session.get(Product, product_id)

    def get_all(self, **filters) -> list[Product]:
        with self.session_factory() as session:
            statement = select(Product)
            for key, value in filters.items():
                if key not in self.UPDATABLE_FIELDS:
                    raise ValueError(f"Product does not have column called '{key}'")
                statement = statement.where(getattr(Product, key) == value)

                return session.scalar(statement).all()

    def get_id_by_name(self, name:str) -> int | None:
        with self.session_factory as session:
            statement = select(Product).where(Product.name == name)
            return session.scalar(statement)

    
                