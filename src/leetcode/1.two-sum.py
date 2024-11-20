# @leet start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)1):
                if i == j:
                    continue
                if nums[i]+nums[j] == target:
                    return [i, j]

            # @leet end
