def list_sum(my_list):
    total = 0
    for element in my_list:
        total += element
    return total


print(f'This is the total {list_sum([4,6,2,29])}')

my_list2 = [4,3,11,11,10,11,11]
print(f'This is the total {list_sum(my_list2)}')
