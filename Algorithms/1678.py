"""
1678. Goal Parser Interpretation
"""


class Solution:
    def interpret(self, command):
        return command.replace('()', 'o').replace('(al)', 'al')


s = Solution()
print(s.interpret("(al)G(al)()()G"))

