#!/usr/bin/python3
def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return False

    # Initialize a set to keep track of opened boxes
    opened_boxes = set([0])

    # Initialize a list to keep track of keys that need to be checked
    keys_to_check = boxes[0]

    # Iterate through the keys to check
    while keys_to_check:
        current_key = keys_to_check.pop()

        # Check if the key opens a new box
        if current_key < len(boxes) and current_key not in opened_boxes:
            opened_boxes.add(current_key)
            keys_to_check.extend(boxes[current_key])

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)

# Example usage:
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
