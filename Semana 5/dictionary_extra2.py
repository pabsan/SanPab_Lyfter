employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
    {"name": "Roy", "email": "roy@empresa.com", "department": "RRHH"}
]

departments_employees = {}

for emp in employees:
    dept = emp.get("department")
    if departments_employees.get(dept) is None:
        departments_employees[dept] = []
    
    departments_employees[dept].append({"name": emp.get("name"),"email":emp.get("email")})

print(departments_employees)
