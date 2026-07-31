class CarsRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_car(self, car_record):
        return {
            "id": car_record[0],
            "brand": car_record[1],
            "model": car_record[2],
            "model_year":car_record[3],
            "status": car_record[4],
            "created_date": car_record[5]
        }

    def validate_status(self, status):
        if status not in ['Dañado','Disponible',"Eliminado","Ocupado","Reparación","Nuevo","Desuso"]:
            return False
        return True
    
    def create(self, brand, model, model_year, status):
        try:
            if not self.validate_status(status):
                return "Error: Invalid status. Must be 'Dañado','Disponible','Eliminado','Ocupado','Reparación','Nuevo' or 'Desuso'."
            result = self.db_manager.execute_query( 
                "CALL lyfter_car_rental.NewCar (%s, %s, %s, %s, NULL, NULL)",
                brand, model, model_year, status
            )
            if result:
                status_message = result[0][0]
                return status_message
        except Exception as error:
            print("Error inserting a car into the database: ", error)
            return str(error)
        
    
    def get_by_id(self, id):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, brand, model, model_year, status, created_date FROM lyfter_car_rental.cars WHERE id = %s", id
            )
            if results:
                return self._format_car(results[0])
            else:
                return None
        except Exception as error:
            print("Error retrieving car by ID from the database: ", error)
            return None
        
    def update(self,id, status):
        try:
            if not self.validate_status(status):
                return "Error: Invalid status. Must be 'Dañado','Disponible','Eliminado','Ocupado','Reparación','Nuevo' or 'Desuso'."
            result = self.get_by_id(id)
            if not result: 
                return "Error: Car with the provided ID does not exist."
            else:
                self.db_manager.execute_query(
                    "CALL lyfter_car_rental.UpdateCar (%s, %s)", id, status
                )
                return "Car status updated successfully"
        except Exception as error:
            print("Error updating car status in the database: ", error)
            return str(error)
