from sqlalchemy.orm import sessionmaker
from Base import Address, User

class AddressRepository:
    UPDATABLE_FIELDS = {
        "street",
        "city",
        "state",
        "zip_code",
        "user_id"
    }

    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def create(self, street: str, city: str, state: str, zip_code: str, user_id: int) -> Address:
            with self.session_factory() as session:
                address = Address(street=street, city=city, state=state, zip_code=zip_code, user_id=user_id)
                session.add(address)
                session.commit()
                return address

    def update(self, address_id: int, **kwargs) -> Address:
            with self.session_factory() as session:
                address = session.get(Address, address_id)
                if not address:
                    raise ValueError(f"Address with id {address_id} does not exist.")

                for key, value in kwargs.items():
                    if key not in self.UPDATABLE_FIELDS:
                        raise ValueError(f"Field '{key}' is not updatable.")
                    setattr(address, key, value)

                session.commit()
                session.refresh(address)
                return address

    def delete(self, address_id: int) -> bool:
            with self.session_factory() as session:
                address = session.get(Address, address_id)
                if not address:
                    return False
                
                session.delete(address)
                session.commit()
                return True