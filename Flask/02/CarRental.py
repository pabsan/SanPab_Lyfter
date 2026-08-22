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
        elif result == "Error: Invalid status. Must be 'Activo', 'Inactivo', 'Eliminado' or 'Moroso'.":
            return jsonify({"error": result}), 400
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
            return jsonify({"error":"No data provided"}),400
        
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
        elif result == "Error: Invalid status. Must be 'Dañado', 'Disponible', 'Eliminado', 'Ocupado', 'Reparación', 'Nuevo' or 'Desuso'.":
            return jsonify({"error":result}),400
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
            return jsonify({"error":"No data provided"}),400
        
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
            return jsonify({"error":"No data provided"}),400
        
        status = data.get("status")
        if status is None or status not in ["Dañado","Disponible","Eliminado","Ocupado","Reparación","Nuevo","Desuso"]:
            return jsonify({"error":"Invalid status. Please verify status. It must be Dañado or Disponible or Eliminado or Ocupado or Reparación or Nuevo or Desuso"}),400
        
        db_manager = open_db_manager()
        if not db_manager:
            return jsonify({"error": "Failed to connect to the database."}), 400
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

@app.route("/cars/<int:car_id>/disable", methods=["PUT"])
def disable_car(car_id):
    try:
        db_manager = open_db_manager()
        if not db_manager:
            return jsonify({"error": "Failed to connect to the database."}), 500
        else:
            cars_repo = CarsRepository(db_manager)
        result = cars_repo.DisableCar(car_id)
        if result == "Car disabled successfully":
            db_manager.close_connection()
            return jsonify({"message": result}), 200
        else:
            db_manager.close_connection()
            return jsonify({"error": result}), 500
    except Exception as error:
        return jsonify({"error": f"Internal server error: {error}"}), 500

@app.route("/users/<int:user_id>",methods=["PUT"])
def update_user(user_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error":"No data provided"}),400
        
        status = data.get("status")
        if status is None or status not in ["Activo","Inactivo","Moroso","Eliminado"]:
            return jsonify({"error":"Invalid status. Please verify status. It must be Activo or Inactivo or Moroso or Eliminado"}),400
        
        db_manager = open_db_manager()
        if not db_manager:
            return jsonify({"error": "Failed to connect to the database."}), 500
        else:
            users_repo = UserRepository(db_manager)
        result = users_repo.update(user_id, status)
        if result == "User updated successfully":
            db_manager.close_connection()
            return jsonify({"message":result}),200
        else:
            db_manager.close_connection()
            return jsonify({"error":result}),500
    except Exception as error:
        return jsonify({"error":f"Internal server error: {error}"}),500

@app.route("/rents/<int:rent_id>/status", methods=["PUT"])
def update_rent_status(rent_id):
    try:
        data = request.get_json(silent=True)

        if not data:
            return jsonify({"error": "No data provided"}), 400

        status = data.get("status")

        if status is None:
            return jsonify({"error": "Status is required"}), 400

        if status not in ["Activo", "Inactivo", "Atraso", "Devuelto"]:
            return jsonify({
                "error": "Invalid status. Please verify status. "
                         "It must be Activo or Inactivo or Atraso or Devuelto"
            }), 400

        db_manager = open_db_manager()

        if not db_manager:
            return jsonify({
                "error": "Failed to connect to the database."
            }), 500

        rents_repo = RentsRepository(db_manager)

        result = rents_repo.update_status(rent_id, status)

        if result == "Rental status updated successfully":
            db_manager.close_connection()
            return jsonify({"message": result}), 200
        else:
            db_manager.close_connection()
            return jsonify({"error": result}), 500

    except Exception as error:
        return jsonify({
            "error": f"Internal server error: {error}"
        }), 500

@app.route("/rents/<int:rent_id>/complete", methods=["PUT"])
def complete_rent(rent_id):
    try:
        db_manager = open_db_manager()

        if not db_manager:
            return jsonify({
                "error": "Failed to connect to the database."
            }), 500

        rents_repo = RentsRepository(db_manager)

        result = rents_repo.update(rent_id)

        if result == "Rental status updated successfully":
            db_manager.close_connection()
            return jsonify({"message": result}), 200
        else:
            db_manager.close_connection()
            return jsonify({"error": result}), 500

    except Exception as error:
        return jsonify({
            "error": f"Internal server error: {error}"
        }), 500


# @app.route("/rents/<int:rent_id>",methods=["PUT"])
# def update_rent(rent_id):
#     try:
#         db_manager = open_db_manager()
#         data = request.get_json(silent=True)
#         status = None
#         if data:
#             status = data.get("status")
#         if not db_manager:
#             return jsonify({"error": "Failed to connect to the database."}), 500
#         else:
#             rents_repo = RentsRepository(db_manager)
#         if status is not None:
#             if status not in ["Activo","Inactivo","Atraso","Devuelto"]:
#                 return jsonify({"error":"Invalid status. Please verify status. It must be Activo or Inactivo or Atraso or Devuelto"}),400
#             result = rents_repo.update_status(rent_id, status)
#         else:
#             result = rents_repo.update(rent_id)
#         if result == "Rental status updated successfully":
#             db_manager.close_connection()
#             return jsonify({"message":result}),200
#         else:
#             db_manager.close_connection()
#             return jsonify({"error1":result}),500
#     except Exception as error:
#         return jsonify({"error2":f"Internal server error: {error}"}),500


@app.route("/users",methods=["GET"])
def get_users():
    try:
        db_manager = open_db_manager()
        user_repo = UserRepository(db_manager)

        filters = request.args.to_dict()
        users = user_repo.get_all(filters)
        db_manager.close_connection()

        return jsonify(users),200
    except Exception as error:
        return jsonify({"error":f"Internal server error: {error}"}),500


@app.route("/cars",methods=["GET"])
def get_cars():
    try:
        db_manager = open_db_manager()
        car_repo = CarsRepository(db_manager)

        filters = request.args.to_dict()
        cars = car_repo.get_all(filters)
        db_manager.close_connection()

        return jsonify(cars),200
    except Exception as error:
        return jsonify({"error":f"Internal server error: {error}"}),500

@app.route("/rents",methods=["GET"])
def get_rents():
    try:
        db_manager = open_db_manager()
        rents_repo = RentsRepository(db_manager)

        filters = request.args.to_dict()
        rents = rents_repo.get_all(filters)
        db_manager.close_connection()

        return jsonify(rents),200
    except Exception as error:
        return jsonify({"error":f"Internal server error: {error}"}),500

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
