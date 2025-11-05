name = input("Type your Name: ")
last_name = input("Type your last name: ")
age = int(input("Type your age: "))

if age < 4:
    print("You're a baby!")
elif age >= 4 and age < 12:
    print("You're a child!")
elif age >= 12 and age < 18:
    print("You're a teenager")
elif age >= 18 and age < 30:
    print("You're a young adult")
elif age >= 30 and age < 60:
    print("You're an adult")
else:
    print("You're an old man")