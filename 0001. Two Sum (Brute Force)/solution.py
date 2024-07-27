class Solution(object):
    def twoSum(self, nums, target):
        result = [0, 0]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result[0] = i
                    result[1] = j
                    return result

        return result
