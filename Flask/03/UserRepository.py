from sqlalchemy.orm import sessionmaker, session
from Base import User

class UserRepository:
    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def create(self, id: int, name: str, last_name: str, status: str, birth_date: str) -> User:
        with self.session_factory() as session:
            user = User(id=id, name=name, last_name=last_name, status=status, birth_date=birth_date)
            session.add(user)
            session.commit()
            return user

    def update(self, user_id: int, **kwargs) -> User:
        with self.session_factory() as session:
            user = session.get(User, user_id)
            if not user:
                raise ValueError(f"User with id {user_id} does not exist.")
            else:
                for key, value in kwargs.items():
                    if hasattr(user, key):
                        setattr(user, key, value)
                    else:
                        raise ValueError(f"User has no attribute '{key}'")
                session.commit()
                return user