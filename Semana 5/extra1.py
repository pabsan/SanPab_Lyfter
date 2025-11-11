list_size = int(input("Enter list length (must be greater than 1): "))
while (list_size < 2):
    list_size= int(input("Enter list length (must be greater than 1): "))

count = 1
count_search = 0
my_list = []
search_number = int(input("Please enter the number to search within the list: "))
while (count <= list_size):
    num = int(input(f"[{count}] Please enter a number: "))
    my_list.append(num)
    count += 1

for element in my_list:
    if (element == search_number):
        count_search += 1

if (count_search > 0):
    print(f"The number {search_number} is {count_search} times.")
else:
    print(f"The number {search_number} was not found.")