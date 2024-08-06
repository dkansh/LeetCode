# 3016. Minimum Number of Pushes to Type Word II

## Overview

The challenge is based on traditional telephone keypads, where each number key `(2-9)` corresponds to a group of
letters.
For example, pressing the key `2` once corresponds to the letter `a`, pressing it twice corresponds to the letter `b`,
and pressing it three times corresponds to the letter `c`.

In this challenge, we can rearrange the letters to the keys as we prefer. Each letter must be assigned to exactly one
key, but a key can have any number of letters (including no letters), and the sets of letters on each key must be
distinct. The goal is to rearrange these letters so that typing the given string `word` requires the fewest key presses.

For instance, for the word `abc`:
If we map it traditionally (where letters a, b, and c are all mapped to key 2), typing would require 1 + 2 + 3 = 6
presses.
However, an optimal remapping might assign each letter to a different key, resulting in just 1 press per letter, for a
total of 3 presses.

## Intuition

To begin, we create an array of size `26` to count the frequency of each character in the word. Each index of the array
represents a character (`a` to `z`), and the value at each index indicates the number of times the corresponding
character appears in the word.

Next, we sort this frequency array in ascending order. Sorting the array helps us efficiently assign key presses to
characters based on their frequencies, starting with the most frequent ones.

We then initialize three variables:

- `i` to traverse the sorted frequency array from the highest frequency
- `count` to track the number of characters assigned to the current key press count
- `multiplier` to represent the current key press count

As we traverse the frequency array from the highest frequency to the lowest, we dynamically assign characters to key
presses. We calculate the product of the frequency of the current character and the current key press
count (`multiplier`) and
add this to our answer (`result`).

We increment the count for each character assigned. When the count reaches 8, indicating the maximum number of
characters assigned to a key press count, we increment the key press count (`multiplier`) and reset the count to 0.

This process continues until all characters are assigned. The total number of key presses required is given by the value
of `result`.

## Algorithm

- Initialize a frequency array:
    - Create an integer array `frequency` of size `26` to store the frequency of each character in the word.
- Count character frequencies:
    - Iterate through each character in the input word.
    - For each character, convert it to its corresponding index (using `char` - `a`) and increment the value at that
      index in the `frequency` array.
- Sort the frequency array:
    - Sort the `frequency` array in ascending order.
- Initialize variables for key press assignment:
    - Set `i` to `25` to start from the end of the sorted frequency array.
    - Initialize `count` to `0` to track the number of characters assigned to the current key press count.
    - Initialize `multiplier` to `1` to represent the current key press count.
    - Initialize `result` to `0` to accumulate the total number of key presses required.
- Assign key presses based on frequency:
    - While `i` is greater than or equal to `0` and a`rr[i]` is not `0`:
        - Add `start * arr[i]` to `result`.
        - Increment `count` by `1`.
        - If `count` reaches `8`:
            - Increment `multiplier` by `1`.
            - Reset `count` to `0`.
        - Decrement `i` by `1`.
- Return the total key presses:
    - Return the value of `result`.

## Complexity Analysis

Let n be the size of string `word`.

- **Time complexity:** `O(n)`
  Going through the word string to count the frequency of each letter takes `O(n)` time.<br /><br />

  Sorting the frequency array, which has a fixed size of 26 (for each letter in the alphabet), takes `O(1)` time because
  the array size is constant.<br /><br />

  Going through the frequency array to calculate the total number of presses takes `O(1)` time due to the constant array
  size.<br /><br />

  In summary, the most significant factor is `O(n)` due to the frequency counting step<br /><br />

- **Space complexity:** `O(1)` Frequency array and sorting require `O(1)` space as it always needs space for 26
  integers.<br /><br />

  In total, the space complexity is `O(1)` because it does not depend on the input size.
