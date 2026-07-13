class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "name": user_record[1],
            "email": user_record[2],
            "username":user_record[3],
            "born_date": user_record[4],
            "password": user_record[5],
            "status": user_record[6],
            "created_date": user_record[7]
        }

    def validate_status(self, status):
        if status not in ['Activo', 'Inactivo', 'Eliminado']:
            return False
        return True
    
    def create(self, name, email, username, born_date, password, status):
        try:
            if not self.validate_status(status):
                return False
            result = self.db_manager.execute_query(
                "CALL lyfter_car_rental.NewUser (%s, %s, %s, %s, %s, %s, NULL)",
                name, email, username, born_date, password, status,
            )
            if result:
                status_message = result[0][0]
                print("Stored procedure returned:", status_message)
                if status_message == "User created successfully":
                    return True
                else:
                    return False
        except Exception as error:
            print("Error inserting a user into the database: ", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, name, email, username, born_date, password, status, created_date FROM lyfter_car_rental.Users;"
            )
            formatted_results = [self._format_user(result) for result in results]
            self.db_manager.close_connection()
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False

    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, full_name, email, password FROM lyfter_duad.users WHERE id = %s;",
                (_id,),
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False

    def update(self, _id, full_name, email, password):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_duad.users SET (full_name, email, password) = (%s, %s, %s) WHERE ID = %s",
                (full_name, email, password, _id),
            )
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False

    def delete(self, _id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_duad.users WHERE id = (%s)", (_id,)
            )
            print("User deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a user from the database: ", error)
            return False