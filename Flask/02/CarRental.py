from flask import Flask, request, jsonify, abort
from Repositories.db import PgManager
from Repositories.UserRepository import UserRepository

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
    

        if not users_repo.create(name, email, username, born_date, password, status):
            return jsonify({"error": "Error creating user. Please make sure all fields are filled correctly. Status must be 'Activo', 'Inactivo' or 'Eliminado'."}), 500
        else:
            db_manager.close_connection()
            return jsonify({"message": "User created successfully"}), 201
    except Exception as error:
        print("Error in post_users: ", error)
        return jsonify({"error": f"Internal server error {error}"}), 500

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
