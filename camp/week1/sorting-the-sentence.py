class Solution:
    def sortSentence(self, s: str) -> str:
        listed = s.split()
        l=[]
        result =[]
        for i in listed:
            l.append(i[-1])
        x=1
        while(x<=len(listed)):
            for j in listed:
                if int(j[-1]) == x:
                    result.append(j[:len(j)-1])
            x+=1
        return (' '.join(result))