class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        x = Counter(arr)
        l = list(x.values())
        l.sort()
        length  = sum(l)
        n = length/2
        c = 0
        while length > n:
            length -= l.pop()
            c+=1
        return (c)


        