"""
1512. Number of Good Pairs
"""
import collections

class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)-1, 0, -1):
            j = i
            for k in range(j):
                if nums[i] == nums[k]:
                    count += 1
        return count

    # def numIdenticalPairs(self, nums):
    #     """
    #     Pretty solution
    #     """
    #     return int(sum(k * (k - 1) / 2 for k in collections.Counter(nums).values()))


s = Solution()
print(s.numIdenticalPairs([1,1,1,1]))
