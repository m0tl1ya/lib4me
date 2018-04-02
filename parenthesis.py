# -*- coding: utf-8 -*-
import itertools


def generate_possible_parenthesis(iterable1, iterable2, r=None):
    """Compute possible parenthesis sequence."""
    pool1 = tuple(iterable1)
    pool2 = tuple(iterable2)
    n = len(pool1) + len(pool2)
    r = n if r is None else r
    for indices in itertools.product(range(2), repeat=r):
        if indices.count(0) == len(pool1):
            zeros = tuple(i for i in range(len(indices)) if indices[i] == 0)
            bst_lis = []
            stack = []
            pivot_1 = 0
            pivot_2 = 0
            for i in range(n):
                if i in zeros:
                    bst_lis.append(pool1[pivot_1])
                    stack.append(pool1[pivot_1])
                    pivot_1 += 1
                else:
                    if '(' in stack:
                        bst_lis.append(pool2[pivot_2])
                        pivot_2 += 1
                        stack.pop()
                    else:
                        break
            if len(bst_lis) == n:
                yield bst_lis


if __name__ == '__main__':
    n = int(input())
    lis = list(generate_possible_parenthesis(['(']*n, [')']*n))
    for l in lis:
        print(','.join(l))
