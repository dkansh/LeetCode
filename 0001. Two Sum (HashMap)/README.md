# 1. Two Sum

## Intuition

The task is to find the indices of two numbers in a list of integers that add up to a specific target.

## Approach

- Use a `HashMap<Integer, Integer>` to store the key as the difference between the target and the current value, and the
  value as the index.
- Iterate through the list of elements from the first to the last.
- Check if the current element value is in the map:
    - If found, return an array of values containing the index retrieved from the map and the current element index.
    - If not found, add the target minus the current element value as a key and the current index as the value, and
      continue the process for the rest of the elements in the array.

## Complexity Analysis

- **Time complexity:** `O(n)`. We traverse the list only once. The hash table reduces the lookup time to O(1), resulting
  in an overall time complexity of O(n)

- **Space complexity:** `O(n)`. The extra space required depends on the number of items stored in the hash table, which
  is exactly n elements.