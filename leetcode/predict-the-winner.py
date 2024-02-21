class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        first = 0

        def find_score(first, last):
            #base case
            if first == last:
                return nums[first]
            firstscore = nums[first] - find_score( first+1, last)
            lastscore = nums[last] - find_score(first, last-1)
            return (max(firstscore, lastscore))

        score_dif=-1
        score_dif=find_score(0,len(nums)-1)
        return score_dif >= 0
        

             


       
