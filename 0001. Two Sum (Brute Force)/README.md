# 1. Two Sum

## Intuition

Given a list of integers, we need to find the indices of the two numbers that add up to a specific target.

## Approach

- Iterate through the list from the first element to the last element.
- Create an inner loop to iterate through the list from the outer loop index+1 to the last element.
- Check if the sum of the values at the outer loop index and inner loop index is equal to the target:
  - If yes, return the array of the indices of the outer loop and inner loop.
  - If no, continue checking for the rest of the elements.

## Complexity Analysis

- **Time complexity:** `O(n^2)`. We have two nested loops iterating through the list of n elements.

- **Space complexity:** `O(1)`. We create an output array of a constant size of 2.