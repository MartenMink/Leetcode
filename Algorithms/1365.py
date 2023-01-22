"""
tasks:
1365. How Many Numbers Are Smaller Than the Current Number
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = [0]*len(nums)
        for ind, item in enumerate(nums):
            result[ind] = sum([True if item > number else False for number in nums])
        return result

s = Solution()
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))
