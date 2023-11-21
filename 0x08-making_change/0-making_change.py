#!/usr/bin/python3

"""Making a change
"""


def makeChange(coins, total):
    """ Determines the fewest amount of coins from coins
    that equals the total amount
    """

    if total <= 0:
        return 0

    remainder = total
    coin_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)

    while remainder > 0:
        if coin_index >= n:
            return -1

        if remainder - sorted_coins[coin_index] >= 0:
            remainder -= sorted_coins[coin_index]
            coin_count += 1

        else:
            coin_index += 1

    return coin_count
