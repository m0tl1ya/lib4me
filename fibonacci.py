# -*- coding: utf-8 -*-

"""
dynamic programming (bottom up)
calculate the number of cases that you ascend a staircase with the stride of
1 or 2 or 3 steps
"""


def triple_step(n):
    """Compute the number of cases of triple steps."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        a = 1
        b = 2
        c = 4
        for i in range(3, n):
            d = a + b + c
            a = b
            b = c
            c = d
        return c


if __name__ == '__main__':
    N = int(input())
    print(triple_step(N))
