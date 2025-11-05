list_size = int(input("Enter list length (must be greater than 1): "))
while (list_size < 2):
    list_size= int(input("Enter list length (must be greater than 1): "))

count = 1
my_list = []

while (count <= list_size):
    num = int(input(f"[{count}] Please enter a number: "))
    my_list.append(num)
    count += 1

negative = False
for element in my_list:
    if element <= 0:
        negative = True

if negative:
    print("There is at least one negative number or zero.")
else:
    print("All numbers are positve")