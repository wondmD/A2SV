class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        first_str = strs[0]

        for i, char in enumerate(first_str):
            for other_str in strs[1:]:
                if i >= len(other_str) or other_str[i] != char:
                    return prefix
            prefix += char

        return prefix