#!/usr/bin/python3
"""Prime Game."""


def isPrime(num):
    if num == 1:
        return False
    for n in range(2, (num // 2) + 1):
        if num % 2 == 0:
            return False
    return True


def choosePrime(arr):
    for num in arr:
        if isPrime(num):
            return num
    return False


def removeMultiples(n, arr):
    out = []
    for num in arr:
        if num % n != 0:
            out.append(num)
    return out


def getPlayer(idx):
    if idx % 2 == 1:
        return 'Maria'
    return 'Ben'


def isWinner(x, nums):
    """Solve the Prime Game Challenge."""
    stats = {'Maria': 0, 'Ben': 0}

    if not x or not nums:
        return None

    for turn in range(x):
        arr = list(range(1, nums[turn] + 1))
        for i in arr:
            prime = choosePrime(arr)
            if prime:
                arr = removeMultiples(prime, arr)
            else:
                winner = getPlayer(i + 1)
                stats[winner] = stats[winner] + 1
                break
    if stats['Maria'] == stats['Ben']:
        return None
    return 'Maria' if stats['Maria'] > stats['Ben'] else 'Ben'
