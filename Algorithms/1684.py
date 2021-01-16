"""
1684. Count the Number of Consistent Strings
"""


class Solution:
    def countConsistentStrings(self, allowed, words):
        return sum([True if len(set(item).difference(allowed)) is 0 else False for item in words])


s = Solution()
print(s.countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))
