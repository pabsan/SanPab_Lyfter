from sqlalchemy import create_engine


DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

try:
    connection = engine.connect()
    print("Connection successful!")
    connection.close()  # Cerramos la conexion cuando terminamos
except Exception as e:
    print("Connection failed:", e)