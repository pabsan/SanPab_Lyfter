my_list = [9, 4, 7, 5, 6, 89, 56, 23, 100, 154, 3]

lowest = my_list[0]

for element in my_list:
    if (element < lowest):
        lowest = element

print(f"The lowest value is {lowest}.")