class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        targetCounter = Counter(p)
        windowCounter = Counter()

        left = right = 0
        while right < len(s):
            windowCounter[s[right]] += 1

            if right - left + 1 > len(p):
                windowCounter[s[left]] -= 1
                if windowCounter[s[left]] == 0:
                    del windowCounter[s[left]]
                left += 1

            if windowCounter == targetCounter:
                result.append(left)

            right += 1

        return result