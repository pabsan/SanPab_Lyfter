list_size = int(input("Enter list length (must be greater than 1): "))
while (list_size < 2):
    list_size= int(input("Enter list length (must be greater than 1): "))

count = 1
my_list = []
list_avg = 0

while (count <= list_size):
    num = int(input(f"[{count}] Please enter a number: "))
    my_list.append(num)
    count += 1
    list_avg += num

list_avg = list_avg / len(my_list)
print(f"Average: {list_avg}")

new_list = []
for element in my_list:
    if (element > list_avg):
        new_list.append(element)

print(f"New list: {new_list}")
