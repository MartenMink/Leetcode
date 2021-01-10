"""
1431. Kids With the Greatest Number of Candies
"""


class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_value = max(candies)
        return [True if item == max_value or (item + extraCandies) >= max_value else False for item in candies]


s = Solution()
print(s.kidsWithCandies([4,2,1,1,2], 1))

