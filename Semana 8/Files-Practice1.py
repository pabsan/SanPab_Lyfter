def open_file(path):
    try:
        with open(path) as file:
            print(file.fileno())
            file_list = []
            for line in file.readlines():
                file_list.append(line)
        return file_list
    except FileNotFoundError as error:
        print(f'Please make sure the file exist. Error: {error}')


def sort_list(my_list):
    n = len(my_list)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if my_list[j].lower() > my_list[j+1].lower():
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


def sort_file(path, my_list):
    sorted_list =  sort_list(my_list)
    try:
        with open(path, 'a') as file:
            for element in sorted_list:
                file.write(element)
    except FileNotFoundError as error:
        print(f'Please make sure the directory is valid. Error: {error}')

song_list = open_file("Song List.txt")
if song_list is not None:
    new_sort_file = 'New Sort Songs.txt'
    with open(new_sort_file,'w') as file:
        pass
    sort_file(new_sort_file,song_list)


