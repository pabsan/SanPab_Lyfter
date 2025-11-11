#Extra 2
count = 1
total = 0
is_number_30 = False
while (count <= 3):
    num = int(input("Please type a number: "))
    total = total + num
    if (num == 30):
        is_number_30 = True
    count += 1

if (is_number_30) or (total == 30) :
    print("Correct")
else:
    print("Incorrect")

