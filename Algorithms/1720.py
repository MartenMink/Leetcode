"""
1720. Decode XORed Array
"""
from itertools import accumulate

class Solution:
    def decode(self, encoded, first):
        result = [None]*(len(encoded) + 1)
        result[0] = first
        for i in range(1, len(encoded) + 1):
            result[i] = result[i-1] ^ encoded[i-1]
        return result

    # def decode(self, encoded, first):
    #     """
    #     Pretty solution
    #     """
    #     return list(accumulate([first] + encoded, lambda x, y: x ^ y))


s = Solution()
print(s.decode([6,2,7,3], 4))
