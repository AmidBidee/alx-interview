#!/usr/bin/python3
"""0-making_change.py
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins: list, total: int) -> int:
    """Return: fewest number of coins needed to meet total

    Args:
        coins [list]: a list of the values of the coins in your possession
        total [int]: the amount in integer to be met
    """
    if total <= 0:
        return 0

    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
