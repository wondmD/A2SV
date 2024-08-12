from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        f_map = defaultdict(list)
        n = len(mat)
        for i in range(n):
            for j in range(len(mat[0])):
                f_map[i+j].append(mat[i][j])
            
        result = []
        for item in f_map:
            if item %2 ==0:
                result+=f_map[item][::-1]
            else :
                result+=f_map[item]
        return (result)