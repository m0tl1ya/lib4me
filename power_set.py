# -*- coding: utf-8 -*-

"""
Compute power set.
"""
import itertools


def compoute_power_set(iterable):
    """Compute power set."""
    yield tuple(())
    pool = tuple(iterable)
    n = len(pool)
    for r in range(1, n+1):
        for tp in itertools.combinations(range(n), r):
            yield tuple(iterable[i] for i in tp)


if __name__ == '__main__':
    lis = list(set([1, 2, 3, 4, 4]))
    for x in compoute_power_set(lis):
        print(x)
