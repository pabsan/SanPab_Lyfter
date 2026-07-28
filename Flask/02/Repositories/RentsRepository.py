class RentsRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_rent(self, rent_record):
        return {
            "id": rent_record[0],
            "user_id": rent_record[1],
            "car_id": rent_record[2],
            "rental_date": rent_record[3],
            "rental_end_date": rent_record[4],
            "return_date": rent_record[5],
            "status": rent_record[6],
            "created_date": rent_record[7]
        }

    def get_by_id(self, id):
            try:
                results = self.db_manager.execute_query(
                    "SELECT id, user_id, car_id, rental_date, rental_end_date, return_date, status, created_date FROM lyfter_car_rental.Rents WHERE id = %s", id
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
