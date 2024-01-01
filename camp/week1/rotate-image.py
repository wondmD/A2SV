class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_lis = matrix.copy()
        matrix.clear()

        for _ in range(len(new_lis)):
            matrix.append([])
        for i in range(len(new_lis)):
            for j in range(len(new_lis[0])):
                # print(l[j][0])
                div_ = j % len(new_lis[0])
                matrix[j].insert(0, new_lis[i][div_])


        return(matrix)