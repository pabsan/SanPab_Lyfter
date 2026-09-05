from sqlalchemy import select, func
from sqlalchemy.orm import sessionmaker
from Base import User, Car

class UserRepository:
    UPDATABLE_FIELDS = {
        "name",
        "last_name",
        "status",
        "birth_date"
    }

    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def create(self, name: str, last_name: str, status: str, birth_date: str) -> User:
        with self.session_factory() as session:
            user = User(name=name, last_name=last_name, status=status, birth_date=birth_date)
            session.add(user)
            session.commit()
            return user

    def update(self, user_id: int, **kwargs) -> User:
        with self.session_factory() as session:
            user = session.get(User, user_id)
            if not user:
                raise ValueError(f"User with id {user_id} does not exist.")
            
            for key, value in kwargs.items():
                if key not in self.UPDATABLE_FIELDS:
                    raise ValueError(f"Field '{key}' is not updatable.")
                setattr(user, key, value)
                
            session.commit()
            session.refresh(user)
            return user

    def delete(self, user_id: int) -> bool:
        with self.session_factory() as session:
            user = session.get(User, user_id)
            if not user:
                return False
            
            session.delete(user)
            session.commit()
            return True

    def get_by_id(self, user_id: int) -> User | None:
        with self.session_factory() as session:
            return session.get(User, user_id)

    def get_all(self, **filters) -> list[User]:
        with self.session_factory() as session:
            statement = select(User)

            for key, value in filters.items():
                if not hasattr(User, key):
                    raise ValueError(f"User has not attribute '{key}'")
                statement = statement.where(getattr(User,key) == value)

            return session.scalars(statement).all()

    def get_users_with_multiple_cars(self):
        with self.session_factory() as session:
            statement = (
                select(
                    User.id,
                    User.name,
                    User.last_name,
                    User.status,
                    User.birth_date,
                    User.created_at,
                    User.updated_at,
                    func.count(Car.id).label("Number_of_Cars")
                )
                .join(Car, User.id == Car.user_id)
                .group_by(
                    User.id,
                    User.name,
                    User.last_name,
                    User.status,
                    User.birth_date,
                    User.created_at,
                    User.updated_at
                )
                .having(func.count(Car.id) > 1)
            )

            return session.execute(statement).all()


    def get_user_data_cars_address(self, user_id: int):
        with self.session_factory() as session:
            user = session.get(User, user_id)

            if not user:
                print(f"User id not found with id: {user_id}.")
                return

            print("---- User data: ----")
            print(f"User id:{user.id}")
            print(f"Name: {user.name} {user.last_name}")
            print(f"Status: {user.status}")

            if not user.cars:
                print("No cars for this user")
            else:
                print("---- Cars data: ----")
                for car in user.cars:
                    print(
                        f"Id: {car.id} "
                        f"Model: {car.model} "
                        f"Brand: {car.brand} "
                        f"Year: {car.year} "
                        f"Status: {car.status}"
                        )
                    
            if not user.addresses:
                print("No addresses for this user")
            else:
                print("---- Addresses data: ----")
                for address in user.addresses:
                    print(
                        f"Id: {address.id} "
                        f"Street: {address.street} "
                        f"City: {address.city} "
                        f"State: {address.state} "
                        f"Zip code: {address.zip_code}"
                    )