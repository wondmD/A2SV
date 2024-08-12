class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,w, wt, val, n):
        
        dp = {}
       
        def nap(idx, w):
            if w <= 0:
               return 0
            if idx>= n:
               return 0
            if (idx, w) in dp:
                return dp[(idx, w)]
            dp[(idx, w)] = max(val[idx] + nap(idx+1, n-wt[idx]), nap(idx+1, n))
            return dp[(idx, w)]
        return nap(0, w)
solver = Solution
