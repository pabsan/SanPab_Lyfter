from flask import Flask, request, jsonify, abort
from Repositories.db import PgManager
from Repositories.UserRepository import UserRepository
from Repositories.CarsRepository import CarsRepository
from Repositories.RentsRepository import RentsRepository

app = Flask(__name__)


def open_db_manager():
    try:
        db_manager = PgManager(
            db_name="lyfter_car_rental",
            user="postgres",
            password="admin123",
            host="localhost"
        )
        return db_manager
    except Exception as error:
        print("Error opening database connection: ", error)
        abort(500, description=f"Internal server error: {error}")

@app.route("/users",methods=["POST"])
def post_users():
    try:
       db_manager = open_db_manager()
       if not db_manager:
            return jsonify({"error": "Failed to connect to the database."}), 500
       else:
        users_repo = UserRepository(db_manager)
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos JSON."}), 400
    
        name = data.get("name")
        email = data.get("email")
        username = data.get("username")
        born_date = data.get("born_date")
        password = data.get("password")
        status = data.get("status")
        
        if not name or not email or not username or not born_date or not password or not status:
            return jsonify({"error": "Missing required fields"}), 400
    
        result = users_repo.create(name, email, username, born_date, password, status)

        if result == "User created successfully":
            db_manager.close_connection()
            return jsonify({"message": result}), 201
        else:
            return jsonify({"error": result}), 500
    except Exception as error:
        print("Error in post_users: ", error)
        return jsonify({"error": f"Internal server error {error}"}), 500


@app.route("/cars",methods=["POST"])
def post_cars():
    try:
        db_manager = open_db_manager()
        if not db_manager:
            return jsonify({"error": "Failed to connect to the database."}), 500
        else:
            cars_repo = CarsRepository(db_manager)
        data = request.get_json()
        if not data:
            return jsonify({"error":"No data provided"}),500
        
        brand = data.get("brand")
        model = data.get("model")
        model_year = data.get("model_year")
        status = data.get("status")

        if not brand or not model or not model_year or not status:
            return jsonify({"error":"Missing required fields"}),400
        
        result = cars_repo.create(brand, model, model_year, status)
        if result == "Car created successfully":
            db_manager.close_connection()
            return jsonify({"message":result}),201
        else:
            return jsonify({"error":result}),500
    except Exception as error:
        return jsonify({"error":f"Internal server error: {error}"}),500
    
@app.route("/rents",methods=["POST"])
def post_rents():
    try:
        db_manager = open_db_manager()
        if not db_manager:
            return jsonify({"error": "Failed to connect to the database."}), 500
        else:
            rents_repo = RentsRepository(db_manager)
        data = request.get_json()
        if not data:
            return jsonify({"error":"No data provided"}),500
        
        user_id = data.get("user_id")
        car_id = data.get("car_id")
        rental_end_date = data.get("rental_end_date")

        if not user_id or not car_id or not rental_end_date:
            return jsonify({"error":"Missing required fields"}),400
        
        result = rents_repo.create(user_id, car_id, rental_end_date)
        if result == "New rental created successfully":
            db_manager.close_connection()
            return jsonify({"message":result}),201
        else:
            return jsonify({"error":result}),500
    except Exception as error:
        return jsonify({"error":f"Internal server error: {error}"}),500
    

@app.route("/cars/<int:car_id>",methods=["PUT"])
def update_car(car_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error":"No data provided"}),500
        
        status = data.get("status")
        if status is None or status not in ["Dañado","Disponible","Eliminado","Ocupado","Reparación","Nuevo","Desuso"]:
            return jsonify({"error":"Invalid status. Please verify status. It must be Dañado or Disponible or Eliminado or Ocupado or Reparación or Nuevo or Desuso"}),500
        
        db_manager = open_db_manager()
        if not db_manager:
            return jsonify({"error": "Failed to connect to the database."}), 500
        else:
            cars_repo = CarsRepository(db_manager)
        result = cars_repo.update(car_id, status)
        if result == "Car status updated successfully":
            db_manager.close_connection()
            return jsonify({"message":result}),200
        else:
            db_manager.close_connection()
            return jsonify({"error":result}),500
    except Exception as error:
        return jsonify({"error":f"Internal server error: {error}"}),500

    
if __name__ == "__main__":
    app.run(host="localhost", debug=True)
