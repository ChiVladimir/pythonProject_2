from sortfunc import insertion_sort, bobble_sort, selection_sort

data_1 = [9, 1, 9, 3, 8, 4, 5, 7, 2, 5, 3, 6, 5, 4, 8, 2, 6, 3, 5, 4]
data_2 = [6, 4, 7, 5, 6, 9, 3, 6, 2, 4, 3, 8, 5, 0, 3, 7]
data_3 = [9, 6, 8, 4, 6, 1, 3, 5, 6, 4, 3, 8, 7, 2, 5, 4, 6, 3, 5, 2, 1, 8, 7, 4, 6]


print(insertion_sort(data_1))
print(insertion_sort(data_2))
print(insertion_sort(data_3))
print("____________________________")

print(bobble_sort(data_1))
print(bobble_sort(data_2))
print(bobble_sort(data_3))
print("____________________________")

print(selection_sort(data_1))
print(selection_sort(data_2))
print(selection_sort(data_3))
