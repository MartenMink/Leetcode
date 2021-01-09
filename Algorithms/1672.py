"""
1672. Richest Customer Wealth
"""


class Solution:
    def maximumWealth(self, accounts):
        return max([sum(item) for item in accounts])


s = Solution()
print(s.maximumWealth([[1, 5], [7, 3], [3, 5]]))
