#!/usr/bin/python3
""" Backtracking the N queens problem. """
from sys import argv


def n_queen(n):
    """Return all possible arrange for the n-queen problem."""
    col = set()
    pos = set()
    neg = set()
    res = []
    state = []

    def backtrack(r):
        """Recurse and do the backtracking."""
        if r == n:
            res.append([val for val in state])
        for c in range(n):
            if c in col or (r + c) in pos or (r - c) in neg:
                continue
            col.add(c)
            pos.add(r + c)
            neg.add(r - c)
            state.append([r, c])

            backtrack(r + 1)

            col.remove(c)
            pos.remove(r + c)
            neg.remove(r - c)
            state.pop()
    backtrack(0)
    return res


def main():
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    if not argv[1].isdigit():
        print('N must be a number')
        exit(1)
    if int(argv[1]) < 4:
        print('N must be at least 4')
        exit(1)
    for res in n_queen(int(argv[1])):
        print(res)


main()
