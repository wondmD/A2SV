class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def distance(x1,y1,x2,y2):
            return abs(x2 - x1) + abs(y2 - y1)
        my_distance = distance(0,0,target[0],target[1])
        x2, y2 = target[0], target[1]
        for i in ghosts:
            x1,y1 = i[0] , i[1]
            if distance (x1,y1,x2,y2)  <= my_distance :
                return False
        return True
        