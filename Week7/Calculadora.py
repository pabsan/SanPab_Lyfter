class InvalidOptionError(Exception):
    def __init__(self):
        super().__init__('Invalid option. Please enter 1-5 number.')


def main():
    try:
        menu()
    except Exception as ex:
        print(f'An unexpected error occurred: {ex}')


def perform_operation(opc,acumlative):
    result = acumlative
    try:
        num= float(input('Enter a number: '))
        match opc:
            case 1:
                result += num
            case 2:
                result -= num
            case 3:
                result = result * num
            case 4:
                try:
                    result = result / num
                except ZeroDivisionError as error:
                    print(f'Error detected in division by zero: {error}')
    except ValueError as error:
        print(f'Invalid number. Try again. {error}')
    return result


def menu():
    num = 0
    result = 0
    option = 0
    while (option != 6):
        print('--------------------')
        print('   Calculator')
        print('[1] Add')
        print('[2] Substract')
        print('[3] Multiply')
        print('[4] Divide')
        print('[5] Delete Result')
        print('[6] Exit')
        try:
            option = int(input('Please enter an option: '))
            if (option <= 0) or (option > 6):
                raise InvalidOptionError()
            elif option == 5:
                result = 0
            elif option < 6:
                result = perform_operation(option,result)
            print(f'Result: {result}')
        except ValueError as error:
            print(f'Invalid option. Error: {error}')
        except InvalidOptionError as e:
            print(f'Error detected: {e}')

if __name__ == '__main__':
    main()
    