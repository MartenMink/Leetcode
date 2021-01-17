"""
1486. XOR Operation in an Array
"""


class Solution:
    def xorOperation(self, n, start):
        element = start
        for i in range(1, n):
            element ^= start + 2*i
        return element


s = Solution()
print(s.xorOperation(10, 5))
