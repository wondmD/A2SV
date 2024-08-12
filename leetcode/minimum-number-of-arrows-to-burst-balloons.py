class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        end = points[0][1]
        tot = 1
        for a,b in points[1:]:
            if a > end:
                tot+=1
                end = b
        return tot