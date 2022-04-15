#!/usr/bin/python3
"""
Lockboxes
"""
import copy


def unlock(keys: list, box: dict) -> bool:
    """
    tries to unlocks a box with available keys
    if it unlocks collect items of box as new keys

    Args:
        keys [list]: list of keys available
        box [dict]: dictionary containing box items and
                    key required to unlock it

    Returns: bool
    """
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

    for i in range(1, len(boxes)):
        u_box = {'key': i, 'items': boxes[i]}
        box.update(**u_box)
        # print(f"box: {box['key']}, available_keys: {available_keys}")
        unlocked = unlock(available_keys, box)
        # print(u_box)
        if unlocked:
            pass
        else:
            locked.append(u_box)

    # print(available_keys)
    if locked:
        still_locked = []
        for i in range(len(locked)):
            # print(f"box: {locked[i]['key']},
            # available_keys: {available_keys}")
            unlocked = unlock(available_keys, locked[i])
            if unlocked:
                pass
            else:
                still_locked.append(locked[i])

        if still_locked:
            return False
    return True
