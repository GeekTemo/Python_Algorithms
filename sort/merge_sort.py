__author__ = 'gongxingfa'


def merge(arr, lo, mid, hi):
    for i in range(lo, hi):
        aux[i] = arr[i]
    i = lo
    j = mid + 1
    k = lo
    while k <= hi:  # or (i < mid or j < hi)
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = aux[j]
            j += 1
        k += 1

def merge_sort(arr):
    pass


arr = [5, 7, 9, 10, 15, 25, 4, 8, 12, 20, 22]

aux = [i for i in arr]
merge(arr, 0, 5, 10)
print arr
