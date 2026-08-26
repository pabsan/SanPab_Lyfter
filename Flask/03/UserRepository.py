from sqlalchemy.orm import sessionmaker, session

class UserRepository:
    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory
