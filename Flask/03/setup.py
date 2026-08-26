from sqlalchemy import create_engine
from Base import Base, User, Address, Car


DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

try:
    connection = engine.connect()
    print("Connection successful!")

    #create the tables in the database
    Base.metadata.create_all(engine)

    connection.close()  # Cerramos la conexion cuando terminamos
except Exception as e:
    print("Connection failed:", e)