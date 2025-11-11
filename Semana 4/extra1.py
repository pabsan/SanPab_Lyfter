def discount(price):
    if (price < 100):
        return price * 0.02
    else:
        return price * 0.10

print("---- Extra 1 ----")
price = int(input("Please enter product price: "))
discount_price = discount(price)
total = price - discount_price
print(f"Total price is {total}")


print("---- Extra 2 ----")
seconds = int(input("Please enter time in seconds: "))
if (seconds < 600):
    remaining = 600 - seconds
    print(f"Remaining seconds {remaining} for 10 minutes")
elif (seconds > 600):
    print("Greater")
else:
    print("Equal")

print("---- Extra 3 ----")
number = input("Please enter a number ")
count = 1
total_num = 0
while (count <= int(number)):
    total_num = total_num + count
    count += 1
print(f"Total is {total_num}")