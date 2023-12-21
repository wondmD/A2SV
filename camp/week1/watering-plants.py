class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        x= capacity
        n = len(plants)
        step = 0
        for i in range(n):
            st = i+1
            if plants[i] <= x:
                step+=1
                x-=plants[i]
            else:
                x = capacity
                step+=(st*2-1)
                x = x-plants[i]
        return (step)