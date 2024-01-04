class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        n = len(names)
        for i in range(n):
            d[heights[i]] = names[i]
        heights.sort(reverse=True)
        for i in range(n):
            names[i] = d[heights[i]]
        return (names)
        