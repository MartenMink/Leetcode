"""
7. Reverse Integer
"""


class Solution:
    def reverse(self, x):
        range_value = 2**31
        result = int(str(x)[::-1]) if x >= 0 else -int(str(x)[1:][::-1])
        if -range_value <= result <= range_value - 1:
            return result
        else:
            return 0


s = Solution()
print(s.reverse(1534236469))
