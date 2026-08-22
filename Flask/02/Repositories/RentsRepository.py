class RentsRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_rent(self, rent_record):
        return {
            "id": rent_record[0],
            "User": rent_record[1],
            "car_brand": rent_record[2],
            "car_model": rent_record[3],
            "rental_date": rent_record[4],
            "rental_end_date": rent_record[5],
            "return_date": rent_record[6],
            "status": rent_record[7],
            "created_date": rent_record[8]
        }

    def get_by_id(self, id):
            try:
                results = self.db_manager.execute_query(
                    """SELECT R.id, U.name as User_Name, C.brand, C.model, R.rental_date, R.rental_end_date, R.return_date, R.status, R.created_date
                                    FROM lyfter_car_rental.Rents AS R
                                    JOIN lyfter_car_rental.Cars AS C
                                        ON R.car_id = C.id
                                    JOIN lyfter_car_rental.users AS U
                                        ON U.id = R.user_id WHERE R.id = %s""", id
                )
                if results:
                    return self._format_rent(results[0])
                else:
                    return None
            except Exception as error:
                print("Error retrieving rent by ID from the database: ", error)
                return None

    def create(self, user_id, car_id, rental_end_date):
        try:
            result = self.db_manager.execute_query(
                "CALL lyfter_car_rental.NewRental (%s, %s, %s, NULL)",
                user_id, car_id, rental_end_date
            )
            if result:
                status_message = result[0][0]
                return status_message
        except Exception as error:
            print("Error inserting a rental into the database: ", error)
            return str(error)

    def get_all(self, filters=None):
            try:
                allowed_filters = {
                    "id":"R.id",
                    "name":"U.name",
                    "brand":"C.brand",
                    "model":"C.model",
                    "rental_date":"R.rental_date",
                    "rental_end_date":"R.rental_end_date",
                    "return_date":"R.return_date",
                    "status":"R.status",
                    "created_date":"R.created_date"
                }
                query = """
                SELECT R.id, U.name as User_Name, C.brand, C.model, R.rental_date, R.rental_end_date, R.return_date, R.status, R.created_date
                FROM lyfter_car_rental.Rents AS R
                JOIN lyfter_car_rental.Cars AS C
                    ON R.car_id = C.id
                JOIN lyfter_car_rental.users AS U
                    ON U.id = R.user_id"""
    
                params = []
    
                if filters:
                    conditions = []
                    for column, value in filters.items():
                        if column not in allowed_filters:
                            continue
                        conditions.append(f"{allowed_filters[column]} = %s")
                        params.append(value)
                if conditions:
                    query += " WHERE " + " AND ".join(conditions)
                    print("Query with filters:", query)

                results = self.db_manager.execute_query(query, *params)
    
                formatted_results = [self._format_rent(result) for result in results]
                self.db_manager.close_connection()
                return formatted_results
            except Exception as error:
                print("Error getting all rents from the database: ", error)
                return False


    def update(self,id):
            try:
                result = self.get_by_id(id)
                if not result:
                    return "Error: Rent with the provided ID does not exist."
                else:
                    if result['status'] == 'Activo' or result['status'] == 'Atraso':
                        self.db_manager.execute_query(
                            "CALL lyfter_car_rental.CarReturn (%s)", id
                        )
                        return "Rental status updated successfully"
                    else:
                        return "Error: Rental is not active and cannot be returned."
            except Exception as error:
                print("Error updating car status in the database: ", error)
                return str(error)


    def update_status(self, id, status):
        try:
            result = self.get_by_id(id)
            if not result:
                return "Error: Rent with the provided ID does not exist."
            else:
                self.db_manager.execute_query(
                    "UPDATE lyfter_car_rental.Rents SET status = %s WHERE id = %s", status, id
                )
                return "Rental status updated successfully"
        except Exception as error:
            print("Error updating rental status in the database: ", error)
            return str(error)
