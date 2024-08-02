class Solution(object):
    def minSwaps(self, nums):
        n = len(nums)
        totalOnes = sum(nums)

        # Edge cases
        if totalOnes == 0 or totalOnes == n:
            return 0

        currentOnes = sum(nums[:totalOnes])
        maxOnes = currentOnes

        # Use two pointers to slide the window
        for i in range(n):
            currentOnes -= nums[i]
            currentOnes += nums[(i + totalOnes) % n]
            maxOnes = max(maxOnes, currentOnes)

        return totalOnes - maxOnes
