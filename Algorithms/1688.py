"""
1688. Count of Matches in Tournament
"""


class Solution:
    # def numberOfMatches(self, n):
    #     """
    #     Unexpected decision :D
    #     """
    #     return n - 1

    def numberOfMatches(self, n):
        count = 0
        while n > 1:
            if n % 2 is 0:
                count += n//2
                n //= 2
            else:
                count += (n - 1)//2
                n = ((n - 1) // 2) + 1
        return count


s = Solution()
print(s.numberOfMatches(14))
