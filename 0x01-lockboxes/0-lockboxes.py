#!/usr/bin/python3
"""Lockboxes | Interview Question"""


def canUnlockAll(boxes):
    # Start with the keys from the first box, which is unlocked
    keys = set(boxes[0])
    # The first box is always unlocked
    unlocked = set([0])

    # Continue until no new boxes can be unlocked
    while True:
        # Keep track of how many boxes we've unlocked in this iteration
        unlocked_this_round = set()

        for key in keys:
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
