def validation(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int,float)):
                raise ValueError(f"Invalid positional argument: {arg}. Must be int or float.")
        for key, value in kwargs.items():
            if not isinstance(value, (int,float)):
                raise ValueError(f"Invalid named argument: {key}={value}. Must be int or float.")
        return func(*args, **kwargs)
    return wrapper

@validation
def add(a, b):
    return a + b

@validation
def substract(a, b):
    return a - b

# Ejemplo de uso
try:
    result_add = add(10, 5)
    print("Resultado de la suma:", result_add)  # Resultado de la suma: 15
    result_substract = substract(10, 5)
    print("Resultado de la resta:", result_substract)  # Resultado de la resta: 5
    #result_invalid = add(10, "five")  # This should raise a ValueError
    other_invalid = substract(4,a=10, b="two")  # This should also raise a ValueError
except ValueError as e:
    print(e)  # Invalid positional argument: five. Must be int or float.