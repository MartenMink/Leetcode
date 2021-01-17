"""
1614. Maximum Nesting Depth of the Parentheses
"""


class Solution:
    def maxDepth(self, s):
        stack = []
        max_value = 0
        for item in s:
            if item is '(':
                stack.append(item)
                if max_value < len(stack):
                    max_value = len(stack)
            elif item is ')':
                stack.pop()
        return max_value


s = Solution()
print(s.maxDepth("1"))
