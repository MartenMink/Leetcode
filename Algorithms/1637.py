"""
1637. Widest Vertical Area Between Two Points Containing No Points
"""

class Solution:
    def maxWidthOfVerticalArea(self, points):
        sort_point = sorted(points, key=lambda x: x[0])
        return max([abs(sort_point[i][0] - sort_point[i+1][0]) for i in range(len(sort_point) - 1)])


s = Solution()
print(s.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
