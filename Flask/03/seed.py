import random
from faker import Faker

from setup import SessionLocal
from UserRepository import UserRepository
from CarRepository import CarRepository
from AddressRepository import AddressRepository

fake = Faker()

def seed_database():
    user_repo = UserRepository(SessionLocal)
    car_repo = CarRepository(SessionLocal)
    address_repo = AddressRepository(SessionLocal)

    users = []

    print("Loading database...")
    print("[##........] 20%")

    for _ in range(20):
        user = user_repo.create(
            name = fake.first_name(),
            last_name=fake.last_name(),
            status=random.choice(["active","inactive"]),
            birth_date=fake.date_of_birth(
                minimum_age=18,
                maximum_age=73
            )
        )

        users.append(user)

        print("[####......] 40%")

        for _ in range(random.randint(1,2)):
            address_repo.create(
                street=fake.street_address(),
                city=fake.city(),
                state=fake.state(),
                zip_code=fake.postalcode(),
                user_id=user.id
            )

        print("[######....] 60%")

        for _ in range(random.randint(1,3)):
            car_repo.create(
                brand=random.choice(["Toyota", "Honda", "Ford", "Chevrolet","BMW","Nissan"]),
                model=fake.word(),
                year=random.randint(2000,2023),
                status=random.choice(["active","inactive"]),
                user_id=user.id
            )

        print("[########..] 80%")

    #Carros sin usuario
    for _ in range(5):
        car_repo.create(
            brand=random.choice(["Toyota", "Honda", "Ford", "Chevrolet","BMW","Nissan"]),
            model=fake.word(),
            year=random.randint(2000,2023),
            status=random.choice(["active","inactive"]),
            user_id=None
        )

    print("[##########] 100%")
    print("Seed Completed Successfully!")
    print(f"Created {len(users)} users.")
    print(f"Created {len(car_repo.get_all())} cars.")
    print(f"Created {len(address_repo.get_all())} addresses.")


if __name__ == "__main__":
    seed_database()
        

    