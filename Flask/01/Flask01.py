from flask import Flask, request, jsonify
from logic import task
from persistance import save_task, get_last_task_id, load_tasks, get_task_by_status, update_task, delete_task, check_task_exists

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Hello, World!</h1>"


@app.route("/information")
def information():
	return {
		"year": 2024,
		"description": "Esto es un endpoint secundario",
	}

task_list = []

@app.route("/task_input", methods=["POST"])
def post_task():

    task_id = request.form.get("id")
    if task_id is not None:
        try:
            task_id = int(task_id)
            if check_task_exists(task_id, "tasks.json"):
                return jsonify({"error": "ID ya existe. Por favor, elija un ID único."}), 400
        except ValueError:
            return jsonify({"error": "ID debe ser un número entero."}), 400
    else:
        task_id = get_last_task_id("tasks.json") + 1
    task_title = request.form.get("title")
    task_description = request.form.get("description")
    task_status = request.form.get("status")
 
    if not task_title or not task_description or not task_status:
          return jsonify({"error": "Missing required fields"}), 400
    
    new_task = task(task_id, task_title, task_description, task_status)
    save_task(new_task, "tasks.json")
    return jsonify(new_task.to_dict()), 201


@app.route("/tasks/all", methods=["GET"])
def get_tasks():
    tasks = load_tasks("tasks.json")
    return jsonify([t.to_dict() for t in tasks]), 200

@app.route("/tasks/status/", methods=["GET"])
@app.route("/tasks/status/<status>", methods=["GET"])
def get_tasks_by_status(status=None):
    if status is None:
        tasks = load_tasks("tasks.json")
        return jsonify([t.to_dict() for t in tasks]), 200
    
    if status not in ['Por Hacer', 'En Progreso', 'Completada']:
        return jsonify({"error": "Estado no válido. Debe ser 'Por Hacer', 'En Progreso' o 'Completada'."}), 400
    tasks = get_task_by_status(status, "tasks.json")
    return jsonify([t.to_dict() for t in tasks]), 200

@app.route("/tasks/update/<int:task_id>", methods=["PUT"])
def update_task_endpoint(task_id):
    task_title = request.form.get("title")
    task_description = request.form.get("description")
    task_status = request.form.get("status")

    if task_status not in ['Por Hacer', 'En Progreso', 'Completada']:
        return jsonify({"error": "Estado no válido. Debe ser 'Por Hacer', 'En Progreso' o 'Completada'."}), 400
    
    if task_title is None and task_description is None or task_title == "" and task_description == "":
        return jsonify({"error": "No se proporcionaron campos para actualizar."}), 400

    success = update_task(task_id, "tasks.json", task_title, task_description, task_status)
    if not success:
        return jsonify({"error": "Tarea no encontrada."}), 404

    return jsonify({"message": "Tarea actualizada correctamente."}), 200


@app.route("/tasks/delete/<int:task_id>", methods=["DELETE"])
def delete_task_endpoint(task_id):
    success = delete_task(task_id, "tasks.json")
    if not success:
        return jsonify({"error": "Tarea no encontrada."}), 404
    return jsonify({"message": "Tarea eliminada correctamente."}), 200


if __name__ == "__main__":
    app.run(host="localhost", debug=True)