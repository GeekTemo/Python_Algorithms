__author__ = 'gongxingfa'


def shell_sort(arr):
    size = len(arr)
    h = 1
    while h < size:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, size):
            j = i
            while j >= h and arr[j] < arr[j - h]:
                arr[j], arr[j - h] = arr[j - h], arr[j]
                j -= h
        h = h / 3
import random
a = [3, 8, 9, 5, 2, 1, 4, 7, 6, 10, 2, 16, 20]
for i in range(10000):
    a.append(random.randint(1, 10000))
shell_sort(a)
print a
