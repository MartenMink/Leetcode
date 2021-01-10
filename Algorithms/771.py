"""
771. Jewels and Stones
"""


class Solution:
    def numJewelsInStones(self, jewels, stones):
        return sum([stones.count(item) for item in jewels])


s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))
