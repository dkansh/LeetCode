# 226. Invert Binary Tree (recursively)

## Intuition

Reversing a singly linked list means we want to change the direction of the pointers so that each node points to its
previous node instead of its next node. Let's break down the problem and the solution intuitively.

### Problem Understanding:

- **Initial List Structure:** In a singly linked list, each node has a reference (or pointer) to the next node.
- **Goal:** Change the direction of these pointers so that each node points to the node before it, effectively reversing
  the list.

## Approach

- Base Case:
    - If the head is null or there is only one node (head.next == null), return the head. This is because a list with
      one or zero elements is already reversed.
- Recursive Step:
    - Recursively call the reverseList function for the next node (head.next).
    - After reversing the rest of the list, set the next node’s next pointer to the current node (head).
    - Set the current node’s next pointer to null to break the original link.
- Return the Reversed List:
    - The recursive calls will return the new head of the reversed list.

## Complexity

- **Time complexity:** `O(n)`. We iterate through the linked list only once.
- **Space complexity:** `O(1)`. We are creating only constant variables.