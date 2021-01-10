"""
1470. Shuffle the Array
"""


class Solution:
    def shuffle(self, nums, n):
        result = [None]*2*n
        result[1::2], result[::2] = nums[:n], nums[n:]
        return result


s = Solution()
print(s.shuffle([1,2,3,4,4,3,2,1],4))
