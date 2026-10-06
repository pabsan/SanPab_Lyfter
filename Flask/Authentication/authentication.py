from db import DB_Manager
from JWT_Manager import JWT_Manager
from flask import Flask, request, Response, jsonify
from autorization import autorization

app = Flask(__name__)


@app.route("/liveness")
def liveness():
    return "<p>Hello World!</p>"


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if (data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        result = db_manager.insert_user(data.get('username'),data.get('password'), data.get('user_type'))
        user_id = result.id

        token = jwt_manager.encode({'id':user_id})
        return jsonify(token=token)

@app.route("/login",methods=["POST"])
def login():
    data = request.get_json()
    if (data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        user_id = db_manager.get_user(data.get('username'),data.get('password'))
        if user_id == None:
            return Response(status=403)
        else:
            token = jwt_manager.encode({'id':user_id})
            return jsonify(token=token)

@app.route("/me")
def me():
    try:
        token = request.headers.get("Authorization")
        if token is not None:
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            user = db_manager.get_user_by_id(user_id)
            return jsonify(id=user_id, username = user.username, user_type = user.user_type)
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)


@app.route("/product", methods=["POST"])
def post_product():
    if not request.is_json:
        return Response("Request must be in JSON format", status=400)
    data = request.get_json()
    if data is None:
        return Response("Invalid JSON", status=400)
    if (data.get('name') == None or data.get('price') == None 
        or data.get('entry_date') == None or data.get('quantity') == None):
        return Response("Missing required fields", status=400)
    else:
        #TODO Validate access
        user_type = autorization.get_user_type(
            request.headers.get("Authorization")
            )

        print(f"======USER TYPE==== {user_type}")

        

        if user_type == "admin":
            result = db_manager.insert_product(data.get('name'),
                                      data.get('price'),
                                      data.get('entry_date'),
                                      data.get('quantity')
                                      )
            product_id = result.id
            return jsonify(id=product_id)
        else:
            return Response("Unauthorized", status=403)


if __name__ == "__main__":
    db_manager = DB_Manager()
    jwt_manager = JWT_Manager('trespatitos','HS256')
    autorization = autorization(jwt_manager,db_manager)
    app.run(host="localhost",debug=True)