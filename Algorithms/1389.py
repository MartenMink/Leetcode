"""
1389. Create Target Array in the Given Order
"""


class Solution:
    def createTargetArray(self, nums, index):
        result = []
        for i in range(len(index)):
            result.insert(index[i], nums[i])
        return result

s = Solution()
print(s.createTargetArray([0], [0]))
