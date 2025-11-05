i = 1

while (i <= 3):
    input_num = int(input("Type a num: "))
    if (i==1):
        high_number = input_num
    elif high_number < input_num:
        high_number = input_num
    i += 1 

print("Highest number " + str(high_number))