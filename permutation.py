#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools


def duplicate_permutation(iterable1, iterable2, r=None):
    """Compute duplicate permutation c!/(a!*b!)."""
    pool1 = tuple(iterable1)
    pool2 = tuple(iterable2)
    n = len(pool1) + len(pool2)
    r = n if r is None else r
    for indices in itertools.product(range(2), repeat=r):
        if indices.count(0) == len(pool1):
            zeros = tuple(i for i in range(len(indices)) if indices[i] == 0)
            bst_lis = []
            pivot_1 = 0
            pivot_2 = 0
            for i in range(n):
                if i in zeros:
                    bst_lis.append(pool1[pivot_1])
                    pivot_1 += 1
                else:
                    bst_lis.append(pool2[pivot_2])
                    pivot_2 += 1
            yield bst_lis


if __name__ == '__main__':
    lis = []
    lis += list(duplicate_permutation([4, 2, 5, 1], [8, 7, 9]))
    print(len(lis))
    lis += list(duplicate_permutation([4, 2, 5, 1], []))
    for li in lis:
        print(li)
    print(len(lis))
    for i in duplicate_permutation([4, 2, 5, 1], [8, 7, 9]):
        print(i)
