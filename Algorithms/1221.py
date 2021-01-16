"""
1221. Split a String in Balanced Strings
"""


class Solution:
    # def balancedStringSplit(self, s: str) -> int:
    #     """
    #     Fun Stack Solution
    #     """
    #     stack, result = [], 0
    #     for c in s:
    #         if stack == []:
    #             result += 1
    #             stack.append(c)
    #         elif c == stack[-1]:
    #             stack.append(c)
    #         else:
    #             stack.pop()
    #     return result
    #
    def balancedStringSplit(self, s):
        count_r, count_l, result = 0, 0, 0
        for ind, item in enumerate(s):
            if item is 'R':
                count_r += 1
            else:
                count_l += 1
            if count_r == count_l:
                result += 1
                count_r, count_l = 0, 0
        return result


s = Solution()
print(s.balancedStringSplit("RLRRRLLRLL"))
