class Solution:
    def maxScore(self, s: str) -> int:
        max_ = zerleft = 0
        count_ones_right = s.count('1')

        for i in range(len(s) - 1):
            zerleft += s[i] == '0'
            count_ones_right -= s[i] == '1'
            max_ = max(max_, zerleft + count_ones_right)

        return max_