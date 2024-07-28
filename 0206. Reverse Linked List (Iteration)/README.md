# 206. Reverse Linked List (iteratively)

## Intuition

To reverse a singly linked list, the goal is to reverse the pointers of the nodes so that the first node becomes the
last one, the second one becomes the second to last one, and so on. The provided solution uses an iterative approach to
accomplish this task.

## Approach

- Initialization:
    - Create a pointer output and initialize it to null. This will eventually be the new head of the reversed list.
- Iteration through the List:
    - Traverse the list using a while loop until the head becomes null.
    - For each node:
        - Store the current head node in a temporary variable temp.
        - Move the head pointer to the next node in the original list.
        - Reverse the pointer of the current node (temp.next) to point to the output list.
        - Move the output pointer to the current node (temp).
- Completion:
    - Once the loop ends, the output pointer will be the head of the reversed list.

## Complexity

- **Time complexity:** `O(n)`. We iterate through the linked list only once.
- **Space complexity:** `O(1)`. We are creating only constant variables.