class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.dp = None
        else:
            rows, cols = len(matrix), len(matrix[0])
            self.dp = [[0] * cols for _ in range(rows)]

            self.dp[0][0] = matrix[0][0]
            for i in range(1, rows):
                self.dp[i][0] = self.dp[i-1][0] + matrix[i][0]
            for j in range(1, cols):
                self.dp[0][j] = self.dp[0][j-1] + matrix[0][j]

            for i in range(1, rows):
                for j in range(1, cols):
                    self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.dp:
            return 0

        total = self.dp[row2][col2]

        if row1 > 0:
            total -= self.dp[row1-1][col2]
        if col1 > 0:
            total -= self.dp[row2][col1-1]
        if row1 > 0 and col1 > 0:
            total += self.dp[row1-1][col1-1]

        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)