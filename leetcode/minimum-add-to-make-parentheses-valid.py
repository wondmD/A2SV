class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == ')' and stack and stack[-1] == '(':
                stack.pop(-1)
            else:
                stack.append(s[i])
        return (len(stack))