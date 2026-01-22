def reverse_buble_sort(my_list):
    n = 0
    i = len(my_list) - 1
    QA1 = 0
    QA2 = 0
    while i >= n:
        modified = False
        j = len(my_list) - 1
        while j >= n:
            if my_list[j] < my_list[i]:
                #cambiar
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
                #modified = True
            j -= 1
            QA2 += 1
        #if not modified:
        #    break
        i -= 1
        QA1 += 1
    print("--> QA1:", QA1, "QA2:", QA2, "List Length:", len(my_list))
    

my_list = [5,3,8,6,2,3,7,4,1]
reverse_buble_sort(my_list)
print(my_list)

my_list2 = ["d","a","c","b","e"]
reverse_buble_sort(my_list2)
print(my_list2)

my_sorted_list = [10,20,30,40,50,100,120,30000]
reverse_buble_sort(my_sorted_list)
print(my_sorted_list)