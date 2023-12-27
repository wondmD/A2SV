class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(1,row-1):
            for j in range(1,col-1):
                sum1 = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                sum2 = grid[i][j]
                sum3 = grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                currunt_sum = sum1+sum2+sum3
                max_sum = max(currunt_sum, max_sum)
        return (max_sum)