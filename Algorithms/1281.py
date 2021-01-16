"""
1281. Subtract the Product and Sum of Digits of an Integer
"""
import numpy as np

class Solution:
    def subtractProductAndSum(self, n):
        l_n = list(map(int, list(str(n))))
        return np.prod(l_n) - np.sum(l_n)


s = Solution()
print(s.subtractProductAndSum(4421))
