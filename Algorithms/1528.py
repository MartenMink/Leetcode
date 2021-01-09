"""
1528. Shuffle String
"""

class Solution:
    def restoreString(self, s, indices):
        return ''.join([item for key, item in sorted(list(zip(indices, s)))])

s = Solution()
print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3]))