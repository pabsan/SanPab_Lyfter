def my_buble_sort(my_list):
    if not isinstance(my_list, list):
        raise TypeError("Input is no a list")
    n = len(my_list)
    i = 0
    QA1 = 0
    QA2 = 0
    while i < n-1:
        modified = False
        j = 0
        while j  < n - 1 - i:
            current = my_list[j]
            current_next = my_list[j+1]
            if current > current_next:
                #cambiar
                my_list[j] = current_next
                my_list[j+1] = current
                modified = True
            j += 1
            QA2 += 1
        if not modified:
            break
        i += 1
        QA1 = i
    print("--> QA1:", QA1, "QA2:", QA2, "List Length:", n)
    

my_list = [5,3,8,6,2,3,7,4,1]
my_buble_sort(my_list)
print(my_list)

my_list2 = ["d","a","c","b","e"]
my_buble_sort(my_list2)
print(my_list2)

my_sorted_list = [10,20,30,40,50,100,120,30000]
my_buble_sort(my_sorted_list)
print(my_sorted_list)