from logic import Task
import json

def get_last_task_id(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            if data:
                return data[-1]['id']
            else:
                return 0
    except FileNotFoundError:
        return 0
    except json.JSONDecodeError:
        return 0
    

def save_task(task, file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    except json.JSONDecodeError:
        data = []
    
    data.append({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status
    })
    
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def load_tasks(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            tasks = []
            for item in data:
                tasks.append(Task(item['id'], item['title'], item['description'], item['status']))
            return tasks
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def get_task_by_status(status, file_name):
    tasks = load_tasks(file_name)
    return [t for t in tasks if t.status == status]


def update_task(task_id, file_name, title=None, description=None, status=None):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return False
    
    task_found = False
    for item in data:
        if item['id'] == task_id:
            if title is not None:
                item['title'] = title
            if description is not None:
                item['description'] = description
            if status in ['Por Hacer', 'En Progreso', 'Completada']:
                item['status'] = status
            task_found = True
            break
    
    if task_found:
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        return True
    else:
        return False
    

def delete_task(task_id, file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return False
    
    for item in data:
        if item['id'] == task_id:
            data.remove(item)
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
            return True
    return False

def check_task_exists(task_id, file_name):
    tasks = load_tasks(file_name)
    for t in tasks:
        if t.id == task_id:
            return True
    return False


