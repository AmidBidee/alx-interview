#!/usr/bin/python3
"""
Lockboxes

Problem definition:
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

The Challenge is to figure out if all boxes[list]
can be unlocked, if so return True else False

Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False

Algorithm:
    functions: [
        unlock: checks if a box key is available, by
                matching it's key with a list of available key,
                if it's unlockable, unlock it and take the items[int]
                in it.

        canUnlockAll: checks if the list of boxes can all be unlocked,
            it calls unlock on each of box in the list, if
            it was unlocked, moves to next box without doing nothing,
            else it logs the locked box in a list of locked boxes.
            if this list remains unoccupied at the end of it's opertion,
            it returns a False, else a True.
    ]
"""


def unlock(keys: list, box: dict) -> bool:
    """
    tries to unlock a box with available keys
    if it unlocks collect items of box as new keys

    Args:
        keys [list]: list of keys available
        box [dict]: dictionary containing box items and
                    key required to unlock it

    Returns: bool
    """
    # takes a key[int] and checks if
    # if matches the box key
    for key in keys:
        if key == box['key']:
            for item in box['items']:
                keys.append(item)
            return True
    return False


def canUnlockAll(boxes: list) -> bool:
    """
    tries to unlock all boxes in a list of box

    Args:
        boxes [list]: list of lists

    Returns: bool
    """

    available_keys = [0]
    locked = []
    box = {
        'key': 0,
        'items': boxes[0]
    }

    unlock(available_keys, box)

    # first traversal on list of boxes
    # it updates the box object with current box
    # passes the box object into unlock()
    # if box was successully unlocked, do nothing
    # else add it to a list of locked boxes
    for i in range(1, len(boxes)):
        u_box = {'key': i, 'items': boxes[i]}
        box.update(**u_box)
        unlocked = unlock(available_keys, box)

        if unlocked:
            pass
        else:
            locked.append(u_box)

    # if locked list is not empty
    # travers the list, and repeat similar
    # if no boxes are left unlocked return to main function
    # else return False
    if locked:
        still_locked = []
        for i in range(len(locked)):
            unlocked = unlock(available_keys, locked[i])
            if unlocked:
                pass
            else:
                still_locked.append(locked[i])

        if still_locked:
            return False
    return True
