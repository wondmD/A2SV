class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_ind = float("inf")
        out =[]
        for i in range(len(list1)):
            if list1[i]  in list2 and i + list2.index(list1[i]) <= min_ind:
                current = i + list2.index(list1[i])
                
                if current < min_ind and out:
                    out.pop()
                out.append(list1[i])
                min_ind=i + list2.index(list1[i])
                
        return (out)

