from flask import Flask, request, jsonify, abort
from Repositories.db import PgManager
from Repositories.UserRepository import UserRepository
from Repositories.CarsRepository import CarsRepository

app = Flask(__name__)

db_manager = PgManager(
    db_name="lyfter_car_rental",
    user="postgres",
    password="admin123",
    host="localhost"
)

@app.route("/users",methods=["POST"])
def post_users():
    try:
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

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
