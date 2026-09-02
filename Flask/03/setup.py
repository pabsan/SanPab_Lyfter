from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Base import Base, User, Address, Car
from UserRepository import UserRepository
from CarRepository import CarRepository
from AddressRepository import AddressRepository


DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'

engine = create_engine(DB_URI, echo=True)

try:
    # Create the tables
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(
        bind=engine,
        expire_on_commit=False
    )

    # ==========================================
    # USER REPOSITORY
    # ==========================================

    user_repo = UserRepository(SessionLocal)

    user1 = user_repo.create(
        name="John",
        last_name="Doe",
        status="active",
        birth_date="1990-01-01"
    )

    user2 = user_repo.create(
        name="Michelle",
        last_name="Smith",
        status="active",
        birth_date="1997-07-17"
    )

    user3 = user_repo.create(
        name="Carlos",
        last_name="Rodriguez",
        status="active",
        birth_date="1988-05-20"
    )

    user4 = user_repo.create(
        name="Sarah",
        last_name="Johnson",
        status="inactive",
        birth_date="1995-11-12"
    )

    print("\nUsers created:")
    print(user1)
    print(user2)
    print(user3)
    print(user4)


    # CAR REPOSITORY
    car_repo = CarRepository(SessionLocal)

    # Asociar el primer auto con el primer usuario
    car1 = car_repo.create(
        brand="Toyota",
        model="Corolla",
        year=2022,
        status="available",
        user_id=user1.id
    )

    # Asociar el segundo auto con el segundo usuario
    car2 = car_repo.create(
        brand="Honda",
        model="Civic",
        year=2021,
        status="available",
        user_id=user2.id
    )

    car3 = car_repo.create(
        brand="Ford",
        model="Mustang",
        year=2023,
        status="rented"
    )

    car4 = car_repo.create(
        brand="Hyundai",
        model="Tucson",
        year=2022,
        status="available"
    )

    car5 = car_repo.create(
        brand="Nissan",
        model="Sentra",
        year=2020,
        status="maintenance"
    )

    car6 = car_repo.create(
        brand="BMW",
        model="X3",
        year=2024,
        status="available"
    )

    print("\nCars created:")
    print(car1)
    print(car2)
    print(car3)
    print(car4)
    print(car5)
    print(car6)


    # TEST UPDATE USER
    updated_user = user_repo.update(
        user_id=user1.id,
        name="Jonathan",
        status="inactive"
    )

    print("\nUpdated user:")
    print(updated_user)


    # TEST UPDATE CAR
    updated_car = car_repo.update(
        car_id=car1.id,
        model="Corolla Hybrid",
        year=2023
    )

    print("\nUpdated car:")
    print(updated_car)


    # TEST DELETE CAR
    deleted = car_repo.delete(car6.id)

    if deleted:
        print("\nCar deleted successfully.")
    else:
        print("\nCar not found.")

    # ADDRESS REPOSITORY
    address_repo = AddressRepository(SessionLocal)

    # CREATE addresses
    address1 = address_repo.create(
        street="123 Main Street",
        city="San Jose",
        state="San Jose",
        zip_code="10101",
        user_id=user1.id
    )

    address2 = address_repo.create(
        street="456 Central Avenue",
        city="Heredia",
        state="Heredia",
        zip_code="40101",
        user_id=user2.id
    )

    address3 = address_repo.create(
        street="789 First Avenue",
        city="Alajuela",
        state="Alajuela",
        zip_code="20101",
        user_id=user3.id
    )

    print("\nAddresses created:")
    print(address1)
    print(address2)
    print(address3)


    # UPDATE ADDRESS
    updated_address = address_repo.update(
        address_id=address1.id,
        street="999 New Main Street",
        city="Escazu",
        zip_code="10203"
    )

    print("\nUpdated address:")
    print(updated_address)


    # DELETE ADDRESS
    deleted = address_repo.delete(address3.id)

    if deleted:
        print("\nAddress deleted successfully.")
    else:
        print("\nAddress not found.")


    # Test select users
    users = user_repo.get_all(
        name="John",
        status="active")

    if users:
        print("\nUsers found:")
        for user in users:
            print(user)

    # Test select cars
    cars = car_repo.get_all(
        brand="Toyota",
        status="available")

    if cars:
        print("\nCars found:")
        for car in cars:
            print(car)

    # Test select addresses
    addresses = address_repo.get_all(
        city="Escazu")

    if addresses:
        print("\nAddresses found:")
        for address in addresses:
            print(address)

except Exception as e:
    print("Setup failed:", e)