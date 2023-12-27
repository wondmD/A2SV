class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        max_a = 0
        for i in range(n-1):
            max_a=max(max_a, points[i+1][0]- points[i][0])
        return (max_a)