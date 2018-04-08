# -*- coding: utf-8 -*-


def compute_cases(n):
    """compute number of cases of payment by DP"""
    if n < 1:
        return 0
    target = 5 * int(n / 5)
    if target == 0:
        return 1
    a = [1]
    for i in range(5, target+1, 5):
        if i >= 25:
            a.append(a[int((i-25)/5)] + a[int((i-10)/5)] + int(i/5) + 1)
        elif i >= 10:
            a.append(a[int((i-10)/5)] + int(i/5) + 1)
        else:
            a.append(int(i/5) + 1)
    return a[-1]


if __name__ == '__main__':
    result = compute_cases(3458)
    print(result)
