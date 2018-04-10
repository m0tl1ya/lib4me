# -*- coding: utf-8 -*-


def binary_search(list, x):
    if (all([i == j for i, j in zip(list, sorted(list))]) == False):
        return None
    low = 0
    high = len(list) - 1
    mid = 0

    while(low <= high):
        mid = int((low + high) / 2)
        if list[mid] < x:
            low = mid + 1
        elif list[mid] > x:
            high = mid - 1
        else:
            return mid

    return None


if __name__ == '__main__':
    lis = [1, 2, 3, 4, 5, 6, 7, 9]
    print(binary_search(lis, 4))
    print(binary_search(lis, 6))
    print(binary_search(lis, 3))
    print(binary_search(lis, 7))
    print(binary_search(lis, 2))
