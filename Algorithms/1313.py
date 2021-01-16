"""
1313. Decompress Run-Length Encoded List
"""


class Solution:
    def decompressRLElist(self, nums):
        return [nums[i+1] for i in range(0, len(nums), 2) for j in range(nums[i])]

s = Solution()
print(s.decompressRLElist([1,2,3,4]))
