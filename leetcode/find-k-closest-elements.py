class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the most closest
        left = 0
        n = len(arr)
        right = n-1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                ans = mid
                break
            elif x < arr[mid]:
                right = mid-1
            else:
                left = mid+1
        
        if ans == 0:
            ans = min(left, right)
        res = []
        if ans<n-1:
            p2 = ans+1
            p1 = ans
        else:
            p2 = ans
            p1 = ans-1
        print (ans)
        for i in range(k):
            if p1 >= 0:
                d1 = abs(arr[p1] - x)
            else:
                d1 = float('inf')
            if p2 < n:
                d2 = abs(arr[p2] - x)
            else:
                d2 = float('inf')
            print (d1, d2)
            if d1 <= d2:
                print (p1)
                res.append(arr[p1])
                p1-=1
            else:
                res.append(arr[p2])
                p2+=1
        res.sort()
        return res

            


