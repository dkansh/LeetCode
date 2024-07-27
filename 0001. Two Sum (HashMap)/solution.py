class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i, num in enumerate(nums):
            if num in map:
                return [map[num], i]
            map[target - num] = i
        return []
        