__author__ = 'gongxingfa'


def insert_sort(arr):
    size = len(arr)
    for i in range(1, size):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and tmp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp


a = [3, 8, 9, 5, 2, 1, 4, 7, 6]
insert_sort(a)
print a
