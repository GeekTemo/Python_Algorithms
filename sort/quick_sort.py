__author__ = 'gongxingfa'


def quick_sort(arr):
    sort(arr, 0, len(arr) - 1)


def exch(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def sort(arr, lo, hi):
    if hi <= lo:
        return
    j = partition(arr, lo, hi)
    sort(arr, lo, j - 1)
    sort(arr, j + 1, hi)


def partition(arr, lo, hi):
    i = lo + 1
    j = hi
    v = arr[lo]
    while True:
        while arr[i] < v and i < hi:
            i += 1
        while arr[j] > v and j > lo:
            j -= 1
        if i >= j:
            break
        exch(arr, i, j)
        i += 1
        j -= 1
    exch(arr, lo, j)
    return j


arr = [10, 7, 9, 20, 15, 25, 4, 8, 12, 20, 2, 50, 10, 19, 20, 57, 11, 90, 20, 56, 3, 5, 9, 10, 29]
partition(arr, 0, len(arr) - 1)
quick_sort(arr)
print arr
