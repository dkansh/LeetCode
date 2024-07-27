# 226. Invert Binary Tree

## Intuition

- Inverting a binary tree means swapping the left and right children of every node.
- This operation can be performed recursively on each node.

## Approach

- A recursive approach is suitable for this problem.
- Base case:
    - If the root is null, return root.
- Swap the left and right children of the current node.
- Recursively invert the left and right subtrees.
- Return the root.

## Complexity

- **Time complexity:** `O(n)`, where n is the number of nodes in the tree. Each node is visited once.
- **Space complexity:** `O(h)`, where h is the height of the tree, due to the recursive call stack.