from sqlalchemy.orm import sessionmaker
from Base import User

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