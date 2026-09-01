from sqlalchemy.orm import sessionmaker
from Base import Car, User

class CarRepository:
    UPDATABLE_FIELDS = {
        "brand",
        "model",
        "year",
        "status",
        "user_id"
    }

    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def create(self, brand: str, model: str, year: int, status: str, user_id: int | None = None) -> Car:
            with self.session_factory() as session:
                car = Car(brand=brand, model=model, year=year, status=status, user_id=user_id)
                session.add(car)
                session.commit()
                return car

    def update(self, car_id: int, **kwargs) -> Car:
            with self.session_factory() as session:
                car = session.get(Car, car_id)
                if not car:
                    raise ValueError(f"Car with id {car_id} does not exist.")

                for key, value in kwargs.items():
                    if key not in self.UPDATABLE_FIELDS:
                        raise ValueError(f"Field '{key}' is not updatable.")
                    setattr(car, key, value)

                session.commit()
                session.refresh(car)
                return car

    def delete(self, car_id: int) -> bool:
            with self.session_factory() as session:
                car = session.get(Car, car_id)
                if not car:
                    return False
                
                session.delete(car)
                session.commit()
                return True