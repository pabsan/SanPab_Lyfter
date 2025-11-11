def is_vocal(my_char):
    vocals = ['a','e','i','o','u']
    for v in vocals:
        if my_char == v:
            return True
    return False

def count_vocals(my_string):
    count = 0
    for element in my_string:
        if is_vocal(element):
            count += 1
    return count

words = input("Enter a string please: ")
print(f"Your string '{words}' has {count_vocals(words)} vocal(s).")
