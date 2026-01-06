def repeat_twice(func):
    def wrapper(name):
        print(f"Hello {name}!")
        print(f"Hello {name}!")
        return func(name)
    return wrapper

@repeat_twice
def greet(name):
    print(f"Nice to meet you, {name}!")

greet("Alyson")

