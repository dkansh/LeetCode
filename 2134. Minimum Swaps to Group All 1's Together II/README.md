# 1653. Minimum Deletions to Make String Balanced

## Overview

We are given a circular array consisting of 0s and 1s. The circular nature of the array means that the last element is
considered adjacent to the first. Our task is to determine the minimum number of swaps needed to group all the 1s
together. A swap involves exchanging values between two distinct positions. Because the array is circular, it offers
more possible groupings compared to a linear array.

For example, given the input: `nums = [0,1,1,1,0,0,1,1,0]`, the output is `2`. This means that two swaps are required to
group all the 1s together, resulting in arrays such as `[1,1,1,0,0,0,0,1,1]` or `[1,1,1,1,1,0,0,0,0]`.

## Intuition

To solve the problem, we need to find the smallest number of swaps needed to group all the 1s in a circular binary array
together. First, we calculate the total count of 1s in the array. If there are no 1s or if the array consists only of
1s, then no swaps are needed, and we can return 0 immediately.

We use a sliding window approach to efficiently identify contiguous subarrays with a high concentration of 1s. We start
by establishing a window covering the first total ones elements of the array and count the number of 1s in this window.
This count serves as our baseline for subsequent comparisons.

Using a two-pointer technique, we move the window across the array and dynamically adjust it to efficiently identify
sequences of 1s. The modulo operation ensures that the window wraps around when it reaches the end of the array,
effectively treating the array as circular. While moving the window, we track the maximum number of 1s found in any
window position. The difference between the total number of 1s and this maximum gives us the minimum number of swaps
required.

## Algorithm

The problem at hand requires us to determine the minimum number of swaps needed to group all 1s in a circular binary
array. The following algorithm details the steps to achieve this, matching the provided Java solution:

- Initialize Variables:
    - Define `n` as the length of the input array `nums`.
    - Initialize `totalOnes` to count the total number of `1`s in the array.
- Count Total 1s:
    - Iterate through the array and sum up all the `1`s to get `totalOnes`.
- Handle Edge Cases:
    - If there are no `1`s `(totalOnes == 0)` or the entire array consists of `1`s `(totalOnes == n)`, return `0` as no
      swaps are needed.
- Initial Window Setup:
    - Initialize `currentOnes` to count the number of `1`s in the first window of size `totalOnes`.
    - Iterate through the first `totalOnes` elements of the array and sum up the `1`s to get `currentOnes`.
- Track Maximum 1s in Window:
    - Initialize `maxOnes` with the value of `currentOnes` to keep track of the maximum number of `1`s found in any
      window position.
- Sliding Window Technique:
    - Use a `for` loop to slide the window across the array:
        - For each position `i` from `0` to `n-1`:
            - Subtract the value of `nums[i]` (element that slides out of the window).
            - Add the value of `nums[(i + totalOnes) % n]` (an element that enters the window) to `currentOnes`.
            - Update `maxOnes` with the maximum value between `maxOnes` and `currentOnes`.
- Calculate Minimum Swaps:
    - The minimum number of swaps required is the difference between `totalOnes` and `maxOnes`.
- Return Result:
    - Return the calculated minimum swaps.

## Complexity Analysis

Let n be the size of string `s`.

- **Time complexity:** `O(n)` The algorithm processes each array element once while expanding and sliding the window,
  resulting in linear time complexity.

- **Space complexity:** `O(1)` The algorithm has constant space complexity regardless of the size of the input array.
