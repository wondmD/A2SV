class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        result=0
        n=len(grid)

        def dfs(i):
            grid[i][i]=2

            for j in range(0,n):
                if grid[i][j]==1:
                    grid[i][j]=2
                    dfs(j)

        for i in range(0,n):
            if grid[i][i]==1:
                result+=1
                dfs(i)

        return result