class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = [i for i in senate]
        count_of_RD = Counter(senate)
        band_r = 0
        band_d = 0
        for i in q:
            if i == "D":
                if band_d > 0:
                   band_d -= 1
                else:
                    count_of_RD['R'] -= 1
                    if count_of_RD['R'] <= 0:
                        return "Dire" 
                    band_r += 1
                    q.append('D') 
            else :
                if band_r > 0:
                   band_r -= 1
                else:
                    count_of_RD['D'] -= 1
                    if count_of_RD['D'] <= 0:
                        return "Radiant" 
                    band_d += 1
                    q.append('R') 
            

