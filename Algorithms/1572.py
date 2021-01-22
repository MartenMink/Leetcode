"""
1572. Matrix Diagonal Sum
"""


class Solution:
    def diagonalSum(self, mat):
        n = len(mat)
        primary = sum([mat[i][i] for i in range(n)])
        secondary = sum([mat[i][n-i-1] for i in range(n)])
        return (primary + secondary) if (n % 2) is 0 else (primary + secondary - mat[n // 2][n // 2])


s = Solution()
print(s.diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))
