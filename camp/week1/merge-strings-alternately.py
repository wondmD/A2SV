class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_l = min(len(word1), len(word2))
        s = ""
        for i in range(min_l):
            s+=word1[i]
            s+=word2[i]
        s+=word1[min_l:]
        s+=word2[min_l:]
        return(s)