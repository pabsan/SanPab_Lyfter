#my_list = [4, 3, 6, 1, 7]

my_list = ["bien","que tal?", "hola"]

if len(my_list) > 1:
    first = my_list[0]
    last = my_list[len(my_list) - 1]
    my_list.pop(0)
    my_list.pop(len(my_list) - 1)
    my_list.insert(0,last)
    my_list.append(first)

print(my_list)
