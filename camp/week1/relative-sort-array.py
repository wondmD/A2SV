class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        f_map = Counter(arr1)
        result = []
        for i in arr2:
            for j in range(f_map[i]):
                result.append(i)
            f_map[i] = 0
        r2 = []
        for i in f_map:
            for j in range(f_map[i]):
                r2.append(i)
            f_map[i] = 0
        r2.sort()
        return (result+r2)
