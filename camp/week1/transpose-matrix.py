class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trps = []
        for i in range(len(matrix[0])):
            trow = []
            for j in range(len(matrix)):
                trow.append(matrix[j][i])
            trps.append(trow)
        return (trps)