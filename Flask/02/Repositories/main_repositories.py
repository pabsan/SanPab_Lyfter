from db import PgManager
from UserRepository import UserRepository


db_manager = PgManager(
    db_name="lyfter_car_rental",
    user="postgres",
    password="admin123",
    host="localhost"
)
users_repo = UserRepository(db_manager)
formatted_results = users_repo.create('John Doe2', 'john.doe7@example.com', 'johndoe7', '1990-01-01', 'password123', 'Activo')

print(formatted_results)