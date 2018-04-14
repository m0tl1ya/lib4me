#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools


def permutation_of_two_iterabele(iterable1, iterable2, r=None):
    """Compute permutation c!/(a!*b!).

    Not consider repetition among iterables.
    """
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


def permutation_of_two_string(iterable1, iterable2, r=None):
    """Compute permutation c!/(a!*b!).

    Not consider repetition among iterables.
    """
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
            yield ''.join(bst_lis)


def permutate_string(string):
    """Permutate string by recursive function."""
    len_s = len(string)
    if len_s == 1:
        return [string]
    elif len_s == 0:
        return []
    else:
        result = []
        c = string[0]
        d = string[1:]
        for i in range(len_s):
            if i == 0:
                for st in permutate_string(d):
                    result.append(c + st)
            elif i == len_s - 1:
                for st in permutate_string(d):
                    result.append(st + c)
            else:
                for st in permutate_string(d):
                    result.append(st[0:i] + c + st[i:])
        return result


def permutate_string_dp(string):
    """Slower than simple permutate_string."""
    len_s = len(string)
    if len_s == 1:
        return [string]
    elif len_s == 0:
        return []
    else:
        result = []
        c = string[0]
        d = string[1:]
        pre_result = permutate_string_dp(d)
        for p in pre_result:
            result += list(permutation_of_two_string(c, p))
        return result


def permutate_sequential(iterable):
    """Commpute permutation in list sequentially."""
    if len(iterable) == 1:
        return iterable
    result = []
    for i, v in enumerate(iterable[0:-1]):
        if i == 0:
            result += list(permutation_of_two_string(iterable[i],
                                                     iterable[i+1]))
        else:
            tmp = []
            for r in result:
                tmp += list(permutation_of_two_string(r, iterable[i+1]))
            result = tmp
    return result


def permutate_string_with_repetition(string):
    """Permutate string considering repetition."""
    stack_single = []
    repetitive_characters = []
    for c in string:
        count = string.count(c)
        if count == 1:
            stack_single.append(c)
        else:
            if c*count not in repetitive_characters:
                repetitive_characters.append(c*count)
    singles = ''.join(stack_single)
    permutation_of_singles = permutate_string(singles)
    permutation_of_repetition = permutate_sequential(repetitive_characters)
    if permutation_of_singles != [] and permutation_of_repetition != []:
        result = []
        for s in permutation_of_singles:
            for t in permutation_of_repetition:
                result += list(permutation_of_two_string(s, t))
        return result
    else:
        if permutation_of_singles != []:
            return permutation_of_singles
        else:
            return permutation_of_repetition


if __name__ == '__main__':
    lis = list(permutation_of_two_iterabele([4, 2, 5, 1], [8, 7, 9]))
    for li in lis:
        print(li)
    print(len(lis))
    # lis = list(permutation_of_two_iterabele([4, 2, 5, 1], [8]))
    print('\n')
    lis = list(permutation_of_two_string('abc', 'def'))
    for li in lis:
        print(li)
    print(len(lis))
    print('\n')

    lis = permutate_string('abc')
    for li in lis:
        print(li)
    print(len(lis))
    print('\n')

    lis = permutate_sequential(['aa', 'bbb', 'cc'])
    for li in lis:
        print(li)
    print(len(lis))
    print('\n')

    lis = list(permutate_string_with_repetition('bbcereraa'))
    print(len(lis))
    print('\n')

    lis = list(permutate_string_with_repetition('bbaac'))
    for li in lis:
        print(li)
    print(len(lis))
