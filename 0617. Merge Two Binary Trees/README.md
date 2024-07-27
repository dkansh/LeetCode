# 617. Merge Two Binary Trees

## Intuition

To merge trees from the root nodes, we can use the depth-first traversal approach. We should add the overlapping nodes
to the result node while keeping the non-overlapping nodes in their original position in the result tree.

## Approach

- A recursive approach is suitable for this problem.
- Base case:
    - If both nodes are null, then return null.
    - If one of the nodes is null, return the other node.
- If both nodes are not null:
    - Create a new node with the value equal to the sum of the input nodes' values.
    - Recursively call the `mergeTrees` function for the left and right children of the input nodes, and set the left
      and right children of the new node to the result of these recursive calls.
    - Return the new node as the result.

## Complexity

- **Time complexity:** `O(n)` n refers to the total number of edges
- **Space complexity:** `O(h)`, where h is the height of the tree, due to the recursive call stack.