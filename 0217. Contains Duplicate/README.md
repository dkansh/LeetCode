# 226. Invert Binary Tree

## Intuition

Given an integer array nums, we want to determine if any value appears at least twice in the array. If at least one value appears more than once, we return true; otherwise, we return false.

## Approach

- Create a set object to store the unique elements that are already traversed.
- Iterate the list from the first element to the last element.
- Check if the current element is already present in the set:
  - If yes, then return true.
  - If no, then add this current element to the set and repeat it for the rest of the elements.

## Complexity

- **Time complexity:** `O(n)`. We iterate through the array only once and the add and get operations on a set are `O(1)`.
- **Space complexity:** `O(n)`. This is the size of the array.