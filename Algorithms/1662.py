"""
1662. Check If Two String Arrays are Equivalent
"""


class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        return ''.join(word1) == ''.join(word2)


s = Solution()
print(s.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))

