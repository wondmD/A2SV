class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1 = len(firstList)
        n2 = len(secondList)
        result = []
        for i in range(n1):
            for j in range(n2):
                pair1 = firstList[i]
                pair2 = secondList[j]
                min1, max1 = pair1[0],pair1[1]
                min2, max2 = pair2[0],pair2[1]
                if min2 <= max1 and min1 <= min2:
                    result.append([min2,min(max1,max2)])
                else:
                    pair2 = firstList[i]
                    pair1 = secondList[j]
                    min1, max1 = pair1[0],pair1[1]
                    min2, max2 = pair2[0],pair2[1]
                    if min2 <= max1 and min1 <= min2:
                        result.append([min2,min(max1,max2)])
        return (result)


            
            