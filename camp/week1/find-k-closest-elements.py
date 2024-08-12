class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dis = []
        for i in arr:
            dis.append((i, abs(i-x)))
        dis.sort(key = lambda x: x[1])
        ans = []
        for i in range(k):
            ans.append(dis[i][0])
        ans.sort()
        return ans