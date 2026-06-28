from flask import Flask, request, jsonify, abort
from logic import Task
from persistance import save_task, get_last_task_id, load_tasks, update_task, delete_task, check_task_exists

app = Flask(__name__)


def throw_error(message, code):
    return abort(code, {"error": message})

@app.route("/tasks", methods=["POST"])
def post_task():

    data = request.get_json()
    if not data:
        return jsonify({"error": "No se proporcionaron datos JSON."}), 400
    
    task_id = data.get("id")
    if task_id is not None:
        try:
            task_id = int(task_id)
            if check_task_exists(task_id, "tasks.json"):
                return jsonify({"error": "ID ya existe. Por favor, elija un ID único."}), 400
        except ValueError:
            return jsonify({"error": "ID debe ser un número entero."}), 400
    else:
        task_id = get_last_task_id("tasks.json") + 1
    task_title = data.get("title")
    task_description = data.get("description")
    task_status = data.get("status")

    if not task_title or not task_description or not task_status:
        return jsonify({"error": "Missing required fields"}), 400
    
    new_task = Task(task_id, task_title, task_description, task_status)
    if new_task.status == "":
        return jsonify({"error": "Estado inválido. Debe ser 'Por Hacer', 'En Progreso' o 'Completada'."}), 400
    save_task(new_task, "tasks.json")
    return jsonify(new_task.to_dict()), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    status_filter = request.args.get("status")
    tasks = load_tasks("tasks.json")
    if status_filter:
        filtered_tasks = list(
            filter(lambda show: show.status == status_filter, tasks)
            )
        return jsonify([t.to_dict() for t in filtered_tasks]), 200
    else:
        return jsonify([t.to_dict() for t in tasks]), 200

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task_endpoint(task_id):

    data = request.get_json()
    if not data:
        return jsonify({"error": "No se proporcionaron datos JSON."}), 400
    
    task_title = data.get("title")
    task_description = data.get("description")
    task_status = data.get("status")

    if task_status is not None and task_status not in ['Por Hacer', 'En Progreso', 'Completada']:
        return jsonify({"error": "Estado no válido. Debe ser 'Por Hacer', 'En Progreso' o 'Completada'."}), 400
    
    if task_title is None and task_description is None or task_title == "" and task_description == "":
        return jsonify({"error": "No se proporcionaron campos para actualizar."}), 400

    success = update_task(task_id, "tasks.json", task_title, task_description, task_status)
    if not success:
        return jsonify({"error": "Tarea no encontrada."}), 404

    return jsonify({"message": "Tarea actualizada correctamente."}), 200


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task_endpoint(task_id):
    success = delete_task(task_id, "tasks.json")
    if not success:
        return jsonify({"error": "Tarea no encontrada."}), 404
    return jsonify({"message": "Tarea eliminada correctamente."}), 200


if __name__ == "__main__":
    app.run(host="localhost", debug=True)