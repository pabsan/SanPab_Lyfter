def string_count(my_str):
    upper = 0
    lower = 0
    for element in my_str:
        if element.islower():
            lower += 1
        elif element.isupper():
            upper += 1  
    print(f"There's {upper} upper cases and {lower} lower cases")


string_count("I love Nación Sushi")
string_count("121212")
string_count("poopopo")
string_count("FGKDJFDKSLJDFi")


