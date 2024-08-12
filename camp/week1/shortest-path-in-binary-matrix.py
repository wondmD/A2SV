class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        leng = len(grid)
        def inb(x, y):
            return 0 <= x < leng and 0<= y <leng
        
        q = deque([(0,0,0)])
        moves = [(0,1),(1,0),(1,1),(-1,0), (0, -1),(-1,-1),(-1,1),(1, -1)]
        ans = float(inf)
        vis = set()
        if grid[0][0]:
            return -1
        while q:
            n = len(q)
            for i in range(n):
                x, y, d = q.popleft()
                if (x, y) == (leng-1,leng-1):
                    print(d)
                    ans = min(ans, d)
                    
                
                for x_, y_ in moves:
                    newx, newy = x + x_, y + y_
                    if inb(newx, newy) and grid[newx][newy] == 0 and (newx, newy) not in vis:
                        q.append((newx, newy, d+1))
                        vis.add((newx, newy))
        if ans != float(inf):
            return ans+1
        return -1
                    




            