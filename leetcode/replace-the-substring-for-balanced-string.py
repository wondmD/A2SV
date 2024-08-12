class Solution:
    def balancedString(self, s: str) -> int:
        avg=len(s)//4
        count=Counter(s)
        extra=""
        
        for ch in count:
            if count[ch]>avg:
                extra+=(count[ch]-avg)*ch
        if not extra:
            return 0
        
        extra_count=Counter(extra)
        left=0
        res=inf
        currnt_freq=Counter()

        for i in range(len(s)):
            currnt_freq[s[i]]+=1
            while extra_count-currnt_freq==Counter():
                res=min(res,i-left+1)
                currnt_freq[s[left]]-=1
                left+=1
        return res
