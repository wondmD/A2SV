class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
    
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            diagonal_moves = min(dx, dy)
            remaining_moves = max(dx, dy) - diagonal_moves
            time = diagonal_moves + remaining_moves
            total_time += time
        
        return total_time