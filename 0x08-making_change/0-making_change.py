#!/usr/bin/python3

""" Greedy Algorithm """

def makeChange(coins, total):
    """ Making change problem. """
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    count = 0
    for coin in coins:
        while coin <= total:
            total -= coin
            count += 1
    return count if (count > 0  and total == 0) else -1
