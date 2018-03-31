# -*- coding: utf-8 -*-


def calculate_undulating_hills(heights):
    """Compute by DP."""
    # extend
    tmp_h = heights + [max(heights)+1]
    dp1 = [None] * len(heights)
    for i in range(len(heights)-1, -1, -1):
        dp1[i] = i + 1
        while tmp_h[dp1[i]] <= tmp_h[i]:
            dp1[i] = dp1[dp1[i]]
    dif1 = [v-i-1 for i, v in enumerate(dp1)]

    # extend
    tmp_h = [max(heights)+1] + heights
    dp2 = [None] * len(heights)
    for i in range(1, len(heights)+1):
        dp2[i-1] = i - 1
        while tmp_h[dp2[i-1]] <= tmp_h[i]:
            dp2[i-1] = dp2[dp2[i-1]-1]
    dif2 = [i-v for i, v in enumerate(dp2)]
    return [i+j for i, j in zip(dif1, dif2)]
