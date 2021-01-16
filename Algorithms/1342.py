"""
1342. Number of Steps to Reduce a Number to Zero
"""


class Solution:
    # def numberOfSteps(self, num):
    #     """
    #     Simple solution
    #     """
    #     count = 0
    #     while num > 0:
    #         if num % 2 is 0:
    #             num //= 2
    #         else:
    #             num -= 1
    #         count += 1
    #     return count

    def numberOfSteps(self, num):
        count = 0
        while num > 0:
            if num & 1 == 1 and num != 1:
                count += 2
            else:
                count += 1
            num = num >> 1
        return count

s = Solution()
print(s.numberOfSteps(14))
