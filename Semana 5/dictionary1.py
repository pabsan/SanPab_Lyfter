name = input("Enter hotel name: ")
stars = int(input("Type number of stars: "))
rooms = int(input("Type number of rooms: "))
floors = int(input("Type number of floors: "))
price = float(input("Type price per night: "))


hotel_info = {
    'name': name,
    'start_number': stars,
    'rooms': [
        rooms,
        floors,
        price
    ]
}

print(hotel_info)