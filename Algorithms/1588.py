"""
1588. Sum of All Odd Length Subarrays
"""


class Solution:
    def sumOddLengthSubarrays(self, arr):
        result = 0
        for i in range(1, len(arr)+1, 2):
            for j in range(0, len(arr)):
                if len(arr) >= j+i:
                    result += sum(arr[j:j+i])
        return result

s = Solution()
print(s.sumOddLengthSubarrays([10,11,12]))
