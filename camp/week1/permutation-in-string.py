class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        s11 = sorted(s1)
        while right <= len(s2):
            if sorted(s2[left:right]) == s11:
                return (True)
            else:
                left+=1
                right +=1
        return (False)

        
        