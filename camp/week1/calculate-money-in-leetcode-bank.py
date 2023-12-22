class Solution:
    def totalMoney(self, n: int) -> int:
        mon = 0
        tot_money = 0
        currunt = 0
        for i in range(1,n+1):
            if i%7 ==1:
                mon += 1
                currunt = mon
                tot_money += currunt
            else:
                currunt += 1
                tot_money+=currunt
                
        return (tot_money)
            