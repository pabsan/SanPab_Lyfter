class Task:
    def validate_status(self, status):
        if status not in ['Por Hacer', 'En Progreso', 'Completada']:
            return False
        return True
    
    def __init__(self, id, title, description, status):
        self.id = id
        self.title = title
        self.description = description
        if self.validate_status(status):
            self.status = status
        else:
            self.status = ''
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }
    
    def __str__(self):  
        return f"ID: {self.id}\nTítulo: {self.title}\nDescripción: {self.description}\nEstado: {self.status}"