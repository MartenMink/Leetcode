"""
1295. Find Numbers with Even Number of Digits
"""


class Solution:
    def findNumbers(self, nums):
        return sum([True if not len(str(item)) % 2 else False for item in nums])


s = Solution()
print(s.findNumbers([555,901,482,1271]))
