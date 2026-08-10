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
        if status not in ['Activo', 'Inactivo', 'Eliminado', 'Moroso']:
            return False
        return True
    
    def create(self, name, email, username, born_date, password, status):
        try:
            if not self.validate_status(status):
                return "Error: Invalid status. Must be 'Activo', 'Inactivo', 'Eliminado' or 'Moroso'."
            result = self.db_manager.execute_query(
                "CALL lyfter_car_rental.NewUser (%s, %s, %s, %s, %s, %s, NULL)",
                name, email, username, born_date, password, status,
            )
            if result:
                status_message = result[0][0]
                return status_message
        except Exception as error:
            print("Error inserting a user into the database: ", error)
            return str(error)

    def get_all(self, filters=None):
        try:
            allowed_filters = {
                "id",
                "name",
                "email",
                "username",
                "born_date",
                "password",
                "status",
                "created_date"
            }
            query = """
            SELECT id, name, email, username, born_date, password, status, created_date
            FROM lyfter_car_rental.Users"""

            params = []

            if filters:
                conditions = []
                for column, value in filters.items():
                    if column not in allowed_filters:
                        continue
                    conditions.append(f"{column} = %s")
                    params.append(value)
                    
                query += " WHERE " + " AND ".join(conditions)

            results = self.db_manager.execute_query(query, *params)

            formatted_results = [self._format_user(result) for result in results]
            self.db_manager.close_connection()
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False

    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, name, email, username, born_date, password, status, created_date FROM lyfter_car_rental.Users WHERE id = %s;",_id
                )
            if results:
                return self._format_user(results[0])
            else:
                return None
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False

    def update(self, id, status):
        try:
            if not self.validate_status(status):
                return "Error: Invalid status. Must be 'Activo', 'Inactivo', 'Eliminado' or 'Moroso'."
            result = self.get_by_id(id)
            if not result:
                return "Error: User with the provided ID does not exist."
            else:
                self.db_manager.execute_query(
                    "CALL lyfter_car_rental.UpdateUser (%s, %s)", id, status
                )
                return "User updated successfully"
        except Exception as error:
            return "Error updating a user from the database: " + str(error)
