import random

def bubble_long_list():
    #arrange
    my_list = []
    i = 1
    for i in range(100):
        random_number = random.randint(1, 100)
        my_list.append(random_number)
    print("Original List:", my_list)

    my_list.sort()
    print("Sorted List:", my_list)

bubble_long_list()