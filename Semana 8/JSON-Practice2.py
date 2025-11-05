import json

class InvalidAnswer(Exception):
    """Invalid input please try again"""
    pass

def print_pokemons(my_list_pokemons):
    for pokemon in my_list_pokemons:
        print(pokemon["name"]['english'])


def read_pokemons(data):
    try:
        my_data = json.loads(data)
        print("You have the following pokemons:")
        print_pokemons(my_data)
        return my_data
    except TypeError as e:
        print(f"Error with JSON: {e}")


def read_pokemons_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        print(f"Error finding the file {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding json data {e}")

def dict_pokemon (name, poke_type, hp, attack, defense, sp_attack, sp_defense, speed):
    new_pokemon = {"name": {
      "english": name
    },
    "type": [
      poke_type
    ],
    "base": {
      "HP": hp,
      "Attack": attack,
      "Defense": defense,
      "Sp. Attack": sp_attack,
      "Sp. Defense": sp_defense,
      "Speed": speed
    }}
    return new_pokemon


def save_to_json(data, filename):
  try:
    with open(filename,'w') as json_file:
      json.dump(data, json_file, indent=4)
    print(f"Successfully converted to json file {filename}")
  except IOError as e:
    print(f"Error saving data file: {e}")


def add_pokemon(data):
    try:
        answer = input("Do you want to add a new pokemon? Y/N ")
        if answer.upper() != 'Y' and answer.upper() != 'N':
            raise InvalidAnswer("Invalid type.")
        if answer.upper() == 'Y':
            name = input("Enter the pokemon name: ")
            poke_type = input("Enter the pokemon type: ")
            print("Now the base info")
            hp = int(input("Type the pokemon HP: "))
            attack = int(input("Type the pokemon attack: "))
            defense = int(input("Type the pokemon defense: "))
            sp_attack = int(input("Type the pokemon Sp Attack: "))
            sp_defense= int(input("Type the pokemon sp Defense: "))
            speed = int(input("Type the pokemon Speed: "))
            new_pokemon = dict_pokemon(name,poke_type,hp,attack,defense,sp_attack,sp_defense,speed)
            data.append(new_pokemon)
            print("New pokemon list ===>")
            print_pokemons(data)
            print("Converting to json again ===>")
            save_to_json(data,'pokemon.json')

    except InvalidAnswer as e:
        print(f"Error on the menu: {e}")
    except ValueError as e:
        print(f"Error on the base: {e}")


def main():
    try:
        my_data = read_pokemons_from_file('pokemon.json')
        if not(my_data is None):
          add_pokemon(my_data)
    except Exception as e:
        print(f"Error: {e}")


main()
