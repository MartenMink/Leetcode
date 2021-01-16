"""
665. Non-decreasing Array
"""


class Solution:
    def checkPossibility(self, nums):
        i, n = 0, len(nums)-1
        result = None
        while i < n:
            if nums[i] > nums[i + 1]:
                if result is not None:
                    return False
                result = i
            i += 1
        return (result is None or result == 0 or result == len(nums)-2 or
                nums[result-1] <= nums[result+1] or nums[result] <= nums[result+2])


s = Solution()
print(s.checkPossibility([2,3,3,2,2]))
