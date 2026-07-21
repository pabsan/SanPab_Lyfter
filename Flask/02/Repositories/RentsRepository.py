class RentsRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_car(self, car_record):
        return {
            "id": car_record[0],
            "user_id": car_record[1],
            "car_id": car_record[2],
            "rental_date": car_record[3],
            "rental_end_date": car_record[4],
            "return_date": car_record[5],
            "status": car_record[6],
            "created_date": car_record[7]
        }

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
