class IsDigitError(Exception):
    def __init__(self):
        super().__init__('Name cannot be numeric')


def ask_name():
    try:
        name = input("Please enter your name: ")
        if name.isdigit():
            raise IsDigitError()
        else:
            return name
    except IsDigitError as error:
        print(f"Error found. {error}")


def ask_age():
    try:
        age = int(input("Please enter you age: "))
        return age
    except ValueError as error:
        print(f"Invalid age. {error}")


def main():
    my_name = ask_name()
    if not(my_name is None):
        my_age = ask_age()
        if not(my_age is None):
            print(f'Hola {my_name}, su edad es {my_age}')


if __name__ == '__main__':
    main()
