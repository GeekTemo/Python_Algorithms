# -*- coding:utf-8 -*-
__author__ = 'gongxingfa'

import math


# 埃拉托色尼筛 法求解小于n的质数
def sieve(n):
    a = dict()
    for p in range(2, n + 1):
        a[p] = p
    for p in range(2, int(math.sqrt(n)) + 1):
        if a[p] != 0:
            j = p * p
            while j <= n:
                a[j] = 0
                j = j + p
    i = 0
    l = []
    for p in range(2, n + 1):
        if a[p] != 0:
            l.append(a[p])
            i = i + 1
    return l


# 使用欧几里得算法就两个数的最大公因数
def euclid_gcd(m, n):
    m, n = (m, n) if m > n else (n, m)
    while n != 0:
        r = m % n
        m, n = n, r
    return m

# 使用连续整数法求
def gcd2(m, n):
    t = m if m < n else n
    while t != 0:
        if m % t == 0 and n % t == 0:
            return t
        else:
            t = t - 1




print gcd2(42, 54)

