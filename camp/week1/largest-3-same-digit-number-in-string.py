class Solution:
    def largestGoodInteger(self, num: str) -> str:
        p = 0
        n = len(num)
        max_sum = float(-inf)
        s = ""
        while p < n-2:
            cur_sum = int(num[p]) +int(num[p+1])+int(num[p+2])
            
            if num[p] == num[p+1] and num[p+1]==num[p+2] and cur_sum>max_sum:
                max_sum = max(max_sum, cur_sum)
                s+= (num[p]+num[p+1]+num[p+2])
            p+=1
        return (s[-3:])
