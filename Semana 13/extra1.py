def repeat_twice(func):
    def wrapper(*args, **kwargs):
        result1 = func(*args, **kwargs)
        result2 = func(*args, **kwargs)
        return result1, result2
    return wrapper

@repeat_twice
def greet(name):
    print(f"Hello, {name}!")


@repeat_twice
def subtract(a, b):
    return a - b

#save data
@repeat_twice
def save_data(data1, data2):
    print(f"Saving data: {data1} and {data2}")

greet("Alyson")
result = subtract(10, 4)
print("Result of subtraction:", result)  # Result of subtraction: 6
save_data("Accoun1", "Account2")