class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        n = len(heaters)
        max_dis = float("-inf")
        for i in houses:
            min_dis = float("inf")

            left = bisect_left(heaters, i)

            if left > 0:
                min_dis = i-heaters[left-1]

            if left < n:
                min_dis = min(min_dis, heaters[left]-i)

            max_dis = max(max_dis, min_dis)
        return max_dis