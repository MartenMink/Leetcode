"""
1534. Count Good Triplets
"""


class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count

s = Solution()
print(s.countGoodTriplets([1,1,2,2,3], 0, 0, 1))
