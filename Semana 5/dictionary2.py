list_a = ["movie_name", "year", "director", "genre"]
list_b = ["Star Wars IV", "1977", "George Lucas", "Science Fiction"]

movie_info = {}
count = 0

for element in list_a:
    movie_info[element] = list_b[count]
    count += 1

print(movie_info)