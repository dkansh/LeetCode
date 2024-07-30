# 1653. Minimum Deletions to Make String Balanced

## Overview

Given a string `s` containing only two characters: `a` and `b`, we need to balance the string by removing any number of
characters. A string is considered "balanced" if there are no occurrences where a `b` is followed by an `a` at any point
later in the string. Our goal is to find the minimum number of deletions required to balance the string.

## Intuition

We keep track of two variables: one to monitor the current minimum deletions and another to count the number of `b`s
encountered up to the current position. As we go through each character in the string, we update these variables
accordingly. This helps us simplify our solution and reduce both time and space complexity. We focus only on the
necessary information required to calculate the minimum deletions efficiently.

## Algorithm

- Initialize `min_deletions` to `0` and `b_count` to `0`.
- Traverse the string from left to right:
    - If the current character is `b`, increment `b_count`.
    - If the current character is `a`, update `min_deletions` as `min(min_deletions + 1, b_count)`.
- Return `min_deletions`.

## Complexity Analysis

Let n be the size of string `s`.

- **Time complexity:** `O(n)` The algorithm performs a single linear pass over the string.

- **Space complexity:** `O(1)` The algorithm uses a constant amount of additional space for min_deletions and b_count.
