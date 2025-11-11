count = 1
my_list = []
while (count < 11):
    my_number = int(input(f"[{count}] Type a number: "))
    my_list.append(my_number)
    if count == 1:
        high = my_number
    elif high < my_number:
        high = my_number
    count += 1

print(f"{my_list} El más alto fue {high}")