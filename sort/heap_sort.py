# -*- coding:utf-8 -*-
__author__ = 'gongxingfa'

import sys
from commcon import less, exch


class Heap(object):
    def _build_heap(self, nums):
        self.size = len(nums)
        self.heap.extend(nums)
        k = self.size / 2
        while k >= 1:
            self._sink(k)
            k -= 1

    def __init__(self, nums=None):
        self.heap = [sys.maxint, ]
        self.size = 0
        if nums:
            self._build_heap(nums)

    def is_empty(self):
        return self.size == 0

    def _swim(self, k):
        while k > 1 and less(self.heap[k / 2], self.heap[k]):
            exch(self.heap, k / 2, k)
            k = k / 2

    def insert(self, v):
        self.size += 1
        self.heap.append(v)
        self._swim(self.size)

    def _sink(self, k):
        while 2 * k <= self.size:
            j = 2 * k
            if j < self.size and less(self.heap[j], self.heap[j + 1]):
                j += 1
            if not less(self.heap[k], self.heap[j]):
                break
            exch(self.heap, k, j)
            k = j

    def delete(self):
        max = self.heap[1]
        exch(self.heap, 1, self.size)
        self.size -= 1
        self._sink(1)
        return max


heap = Heap([16, 7, 3, 20, 17, 8, 2, 10, 9, 25, 67, 35, 22])

print heap.delete()
print heap.delete()
print heap.delete()
print heap.delete()
print heap.delete()
print heap.delete()
