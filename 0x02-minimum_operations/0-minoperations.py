#!/usr/bin/python3
"""
minimum operations challenge.
...
"""


def minOperations(n):
    """
    Computes the fewest number of operations needed to give
    exactly n H characters.
    """
    if not isinstance(n, int):
        return 0
    op_count = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            op_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            op_count += 2
        elif clipboard > 0:
            # paste
            done += clipboard
            op_count += 1
    return op_count
