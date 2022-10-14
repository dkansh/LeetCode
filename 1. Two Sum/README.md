# Two Sum
## Algorithm

We need a efficient way to check if the complement exists in the array. If the complement exists, we need to get its index. What is the best way to maintain a mapping of each element in the array to its index? A hash table.
We add each element's value as a key and its index as a value to the hash table. While we are iterating and inserting elements into the hash table, we also look back to check if current element's complement `(target−nums[i])` already exists in the hash table. If it exists, we have found a solution and return the indices immediately. 
Beware that the complement must not be `nums[i]` itself!

## Complexity Analysis

**Time complexity:** `O(n)`. We traverse the list containing nnn elements exactly twice. Since the hash table reduces the lookup time to `O(1)`, the overall time complexity is `O(n)`.

**Space complexity:** `O(n)`. The extra space required depends on the number of items stored in the hash table, which stores exactly nnn elements.