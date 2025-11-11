def minimum_letters (my_list, minimum):
    new_list = []
    for element in my_list:
        if len(element) > minimum:
            new_list.append(element)
    return new_list

words = ["cielo", "sol", "maravilloso", "día","gato"]
minimum = int(input("Enter minimum character number: "))
print(f"Word with more than {minimum} are {minimum_letters(words,minimum)}")