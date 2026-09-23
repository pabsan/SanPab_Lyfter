from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from Base import User

class UserRepository:
    UPDATABLE_FIELDS = {
        "username",
        "password"
    }

    def __init__(self, session_factory : sessionmaker):
        self.session_factory = session_factory

    def create(self, username: str, password: str) -> User:
        with self.session_factory() as session:
            user = User(username = username, password=password)
            session.add(user)
            session.commit()
            return user

    def update(self, user_id: int, **kwargs) -> User:
        with self.session_factory() as session:
            user = session.get(User, user_id)
            if not user:
                raise ValueError(f"User Id with {user_id} does not exists")

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

    def get_by_id(self, user_id : int) -> User | None:
        with self.session_factory() as session:
            return session.get(User, user_id)

    def get_all(self, **filters) -> list[User]:
        with self.session_factory() as session:
            statement = select(User)

            for key, value in filters.items():
                if key not in self.UPDATABLE_FIELDS:
                    raise ValueError(f"User does not have attribute {key}")
                statement = statement.where(getattr(User,key) == value)

            return session.scalar(statement).all()

    def get_id_by_username(self, username: str) -> int | None:
        with self.session_factory() as session:
            statement = select(User.id).where(User.username == username)
            return session.scalar(statement)