def string_count(my_str):
    upper = 0
    lower = 0
    for element in my_str:
        if element.islower():
            lower += 1
        elif element.isupper():
            upper += 1  
    return f"There's {upper} upper cases and {lower} lower cases"


print(string_count("I love Nación Sushi"))
print(string_count("121212"))
print(string_count("poopopo"))
print(string_count("FGKDJFDKSLJDFi"))
