#!/usr/bin/python3

"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None
    max_number = max(nums)
    filter_list = [True for _ in range(max(max_number + 1, 2))]
    print(filter_list)
    for i in range(2, int(pow(max_number, 0.5)) + 1):
        if not filter_list[i]:
            continue
        for j in range(i*i, max_number + 1, i):
            filter_list[j] = False
    filter_list[0] = filter_list[1] = False
    c = 0
    for i, is_prime in enumerate(filter_list):
        if is_prime:
            c += 1
        filter_list[i] = c
    p1 = 0
    for n in nums:
        p1 += filter_list[n] % 2 == 1
    if p1 * 2 == len(nums):
        return None
    if p1 * 2 > len(nums):
        return "Maria"
    return "Ben"
