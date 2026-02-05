def reverse_string(my_string):
    i = len(my_string) - 1 
    my_var = ""
    while (i >= 0):
        my_var += my_string[i]
        i -= 1
    return my_var


song = 'Enter Sadman'
print(f'Enter Sadman is {reverse_string(song)} backwards.')
