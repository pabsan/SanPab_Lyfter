def count_chars (my_string, my_char):
    count = 0
    for element in my_string:
        if element == my_char:
            count += 1
    return count

my_var = input("Enter a text: ")
search = input("Enter character to look for: ")

print(f"The character '{search}' in text '{my_var}' was found {count_chars(my_var,search)} time(s).")

