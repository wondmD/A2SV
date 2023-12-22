class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        out = s[:spaces[0]]
        for i in range(len(spaces)-1):
            
            out += " " + s[spaces[i]:spaces[i+1]]
        out += " " + s[spaces[-1]:]
        return (out)