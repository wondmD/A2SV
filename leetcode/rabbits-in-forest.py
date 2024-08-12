class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = defaultdict(int)
        tot = 0

        for i in answers:
            if dic[i] > 0 and dic[i] < i+1:
                dic[i] += 1
            elif dic[i] == i+1:
                tot += i+1

                dic[i] = 1
            else:
                tot += i+1
                dic[i] +=1
        return (tot)
