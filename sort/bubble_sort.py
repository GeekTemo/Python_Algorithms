__author__ = 'gongxingfa'


def bubble_sort(arr):
    size = len(arr)
    for i in range(0, size - 1):
        for j in range(0, size - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

a = [3, 8, 9, 5, 2, 1, 4, 7, 6]
bubble_sort(a)
print a
