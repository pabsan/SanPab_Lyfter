from JWT_Manager import JWT_Manager
from db import DB_Manager

class autorization:
    def __init__(self, jwt_manager, db_manager):
        self.jwt_manager = jwt_manager
        self.db_manager = db_manager

    def get_user_bytoken(self, token: str) -> int | None:
        try:
            print(f"======TOKEN==== {token}")
            if token is not None:
                token = token.replace("Bearer ", "")
                decoded = self.jwt_manager.decode(token)
                user_id = decoded['id'] 
                if user_id:
                    return user_id
                else:
                    return None
            else:
                return None
        except Exception as e:
            print(f"======ERROR==== {e}")
            return None

    def get_user_type(self, token: str) -> str | None:
        try:
            user_id = self.get_user_bytoken(token)
            print(f"======USER ID==== {user_id}")
            user = self.db_manager.get_user_by_id(user_id)
            if user:
                return user.user_type
            else:
                return None
        except Exception as e:
            return None
