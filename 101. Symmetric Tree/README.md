# 101. Symmetric Tree

## Intuition

- A symmetric tree is a mirror image of itself.
- To check for symmetry, we can compare the left subtree with the right subtree.
- If they are mirror images of each other, the tree is symmetric.

## Approach

- Create a helper function `helper` to check if two trees are mirror images.
    - Base cases:
        - If both trees are null, return true.
        - If only one tree is null, return false.
    - Check if the root values of both trees are equal.
    - Recursively check if the left subtree of the first tree is a mirror image of the right subtree of the second tree.
    - Recursively check if the right subtree of the first tree is a mirror image of the left subtree of the second tree.
- In the isSymmetric function:
    - If the root is null, return true.
    - Call the `helper` function to check if the left and right subtrees of the root are mirror images.

## Complexity

- **Time complexity:** O(n), where n is the number of nodes in the tree. Each node is visited once.
- **Space complexity:** O(h), where h is the height of the tree, due to the recursive call stack.