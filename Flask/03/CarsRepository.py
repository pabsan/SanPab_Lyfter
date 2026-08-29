from sqlalchemy.orm import sessionmaker
from Base import Car

class CarRepository:
    UPDATABLE_FIELDS = {
        "brand",
        "model",
        "year",
        "status"
    }

    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def create(self, brand: str, model: str, year: int, status: str) -> Car:
            with self.session_factory() as session:
                car = Car(brand=brand, model=model, year=year, status=status)
                session.add(car)
                session.commit()
                return car
