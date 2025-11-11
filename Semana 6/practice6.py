def convert_to_list (my_str):
    my_list = []
    str_output = ""
    for element in my_str:
        if element == "-" and str_output != "":
            my_list.append(str_output)
            str_output = ""
        else:
            str_output += element
    if str_output != "":
        my_list.append(str_output)
    return my_list


def sort_list(my_list):
    n = len(my_list)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if my_list[j].lower() > my_list[j+1].lower():
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

the_string = "python-variable-funcion-computadora-monitor"
#the_string = "llave-llavero-muestra-zinc-Yoda-123"
the_list = convert_to_list(the_string)
print(sort_list(the_list))
