"""
832. Flipping an Image
"""


class Solution:
    def flipAndInvertImage(self, A):
        reversed_a = [item[::-1] for item in A]
        result = []
        for item in reversed_a:
            result.append([0 if letter is 1 else 1 for letter in item ])
        return result


s = Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))

