class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            pr = self.generate(numRows - 1)
            nr = [1] * numRows
            for i in range(1, numRows - 1):
                nr[i] = pr[-1][i - 1] + pr[-1][i]
            pr.append(nr)
            return pr
