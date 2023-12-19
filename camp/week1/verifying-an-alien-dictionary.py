class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_map = {}
        for i, char in enumerate(order):
            char_map[char] = i
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if char_map[word1[j]] < char_map[word2[j]]:
                    break
                elif char_map[word1[j]] > char_map[word2[j]]:
                    return False
            else:
                if len(word1) > len(word2):
                    return False
        return True