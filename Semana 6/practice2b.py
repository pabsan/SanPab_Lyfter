global_variable = 8


def function_1():
    global global_variable
    global_variable = 10
    print(f"This is the second value of global {global_variable}")

print(f"This is the first value of global {global_variable}")
function_1()