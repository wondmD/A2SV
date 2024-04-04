class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        graph = {
            (1,(0,1)) : [3,5,1],
            (1,(0,-1)) : [4,6,1],
            (2,(1,0)) : [5,6,2],
            (2,(-1,0)) : [3,4,2],
            (3,(1,0)) : [2,5,6],
            (3,(0,-1)) : [1,4,6],
            (4,(1,0)) : [2,6,5],
            (4,(0,1)) : [1,3,5],
            (5,(-1,0)) : [2,3,4],
            (5,(0,-1)) : [1,4,6],
            (6,(0,1)) : [1,3,5],
            (6,(-1,0)) : [2,3,4],

        }

        directions = [(0,1),(-1,0),(1,0),(0,-1)]
        moves ={
            1 : [directions[0], directions[3]],
            2 : [directions[1], directions[2]],
            3 : [directions[2], directions[3]],
            4 : [directions[0], directions[2]],
            5 : [directions[3], directions[1]],
            6 : [directions[1], directions[0]],          
        }
        visited = set()
        def inbound(row, col):
            return 0<= row < len(grid) and 0<= col < len(grid[0])
        ans = False
        def dfs(row, col):
            nonlocal ans
            if (row, col) in visited or not inbound:
                return 
            if row == len(grid)-1 and col == len(grid[0])-1:
                ans = True
                return 
            visited.add((row, col))
            for row_change, col_change in moves[grid[row][col]]:
                new_row = row + row_change
                new_col = col + col_change
                
                x = inbound(new_row, new_col)  
                v = (new_row, new_col) in visited
               
                if x and (not v) and (grid[new_row][new_col] in graph[(grid[row][col],(row_change,col_change))]):
                    # print(new_row, new_col)
                    # print(grid[row][col], graph[(grid[row][col],(row_change,col_change))])
                    # print("-", grid[new_row][new_col])
                    dfs(new_row, new_col)
        dfs(0,0)
        return ans



