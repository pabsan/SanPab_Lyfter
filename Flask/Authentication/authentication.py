from db import DB_Manager
from JWT_Manager import JWT_Manager
from flask import Flask, request, Response, jsonify

app = Flask(__name__)


@app.route("/liveness")
def liveness():
    return "<p>Hello World!</p>"


if __name__ == "__main__":
    db_manager = DB_Manager()
    jwt_manager = JWT_Manager('trespatitos','HS256')
    app.run(host="localhost",debug=True)