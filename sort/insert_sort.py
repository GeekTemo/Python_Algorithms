__author__ = 'gongxingfa'

def insert_sort(arr):
    result = [arr[0], ]
    for i in range(1, len(arr)):
        key = arr[i]
        j = len(result) - 1
        while j >= 0 and result[j] > key:
            j = j - 1
        result.insert(j + 1, key)
    return result



a = [2, 3, 20, 10, 5, 2, 1, 4, 7, 6]
a = insert_sort(a)
print a



