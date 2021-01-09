"""
1480. Running Sum of 1d Array
"""


class Solution:
    def runningSum(self, nums):
        return [sum(nums[:i]) for i in range(1, len(nums) + 1)]


s = Solution()
print(s.runningSum([3, 1, 2, 10, 1]))
