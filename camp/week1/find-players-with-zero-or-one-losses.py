class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        my_dic={}
        for i in matches:
            if i[1] not in my_dic:
                my_dic[i[1]]=1
            else:
                my_dic[i[-1]]+=1
        temp=set()
        for x in matches:
            if x[0] not in my_dic:
                temp.add(x[0])
        temp_2=[]
        for x in my_dic:
            if my_dic[x]==1:
                temp_2.append(x)
        temp=list(temp)
        res=[]
        temp.sort()
        temp_2.sort()
        res.append(temp)
        res.append(temp_2)
        return res