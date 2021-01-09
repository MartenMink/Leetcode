"""
1329. Sort the Matrix Diagonally
"""
import collections

class Solution:
    def diagonalSort(self, mat):
        n, m = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[i - j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse=True)
        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i - j].pop()
        return mat


s = Solution()
print(s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
