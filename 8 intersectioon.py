def intersection(list1, list2):
    return list(set(list1) & set(list2))

list1 = [7, 3, 2, 4, 8]
list2 = [5, 3, 4, 8, 2]
print(intersection(list1, list2))