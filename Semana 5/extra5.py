count = 1
my_list = []

while (count <= 5):
    word = input(f"[{count}] Please enter ay word: ")
    my_list.append(word)
    count += 1

new = []
for e in my_list:
    if(len(e) > 4):
        new.append(e)

if len(new) > 0:
    print(new)
else:
    print("There are no words with more than 4 letters")