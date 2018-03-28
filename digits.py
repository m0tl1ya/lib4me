# -*- coding: utf-8 -*-


def find_digits(main_str, seq, stack, index, K):
    if index < len(main_str):
        results = []
        for i in range(0, 10):
            tmp_stack = stack[:]
            if str(i) not in tmp_stack:
                tmp_stack.append(str(i))
            if len(tmp_stack) <= K:
                if str(i) == main_str[index]:
                    results.append(find_digits(main_str, seq+str(i),
                                   tmp_stack, index + 1, K))
                else:
                    multiplied = len(main_str)-index-1
                    if str(i) < main_str[index]:
                        if len(tmp_stack) == K and tmp_stack != ['0']:
                            new_digits = \
                                str(max([int(i) for i in tmp_stack])) * \
                                multiplied
                        else:
                            new_digits = '9' * multiplied
                    else:
                        if len(tmp_stack) == K:
                            new_digits = \
                                str(min([int(i) for i in tmp_stack])) * \
                                multiplied
                        else:
                            new_digits = '0' * multiplied
                    results.append(int(seq + str(i) + new_digits))
            else:
                pass
        diff = [abs(int(digits) - int(main_str)) for digits in results]
        opt_index = diff.index(min(diff))
        return results[opt_index]
    else:
        return int(seq)


if __name__ == '__main__':
    a, k = map(int, input().split())
    a_str = str(a)
    output = find_digits(a_str, seq='', stack=[], index=0, K=k)
    # print(abs(output - a))
