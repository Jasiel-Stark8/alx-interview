#!/usr/bin/python3
"""Lockboxes | Interview Question"""


def canUnlockAll(boxes):
    """
    Determine if all lockboxes can be opened.

    This method checks if all lockboxes can be opened given a list of lockboxes, \
        where each lockbox contains keys to other lockboxes. \
            The first lockbox (index 0) is always unlocked. \
                The method iterates over the lockboxes using the keys obtained to \
                    unlock as many additional lockboxes as possible.

    Parameters:
    boxes (list of list of int): A list where each element is a list of integers \
        representing the keys contained in that lockbox.

    Returns:
    bool: True if all lockboxes can be unlocked using the keys available, False otherwise.

    Example:
    >>> canUnlockAll([[1], [2], [3], [4], []])
    True
    >>> canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
    False
    """
    # Start with the keys from the first box, which is unlocked
    keys = set(boxes[0])
    # The first box is always unlocked
    unlocked = set([0])

    # Continue until no new boxes can be unlocked
    while True:
        # Keep track of how many boxes we've unlocked in this iteration
        unlocked_this_round = set()

        for key in list(keys):  # Iterate over a copy of the keys
            if key < len(boxes) and key not in unlocked:
                unlocked_this_round.add(key)
                # Add new keys from the unlocked box
                keys.update(boxes[key])

        # Update the unlocked boxes
        unlocked.update(unlocked_this_round)

        # If we didn't unlock any new boxes, we're done
        if not unlocked_this_round:
            break

    # If we've unlocked all boxes, return True
    return len(unlocked) == len(boxes)
