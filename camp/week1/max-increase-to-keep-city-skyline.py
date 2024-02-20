class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_rows = []
        max_cols = []
        incrmnt = 0
        trans = list(zip(*grid))
        for i in range(len(grid)):
                max_rows.append(max(grid[i]))
                max_cols.append(max(trans[i]))

        for i in range(len(grid)):
            for j in range(len(grid)):
                val = min(max_rows[i],max_cols[j])-grid[i][j]
                if val:
                    incrmnt += val

        return incrmnt
         
        #time complexity O(n^2)
        #space complexity O(n)