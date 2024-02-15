class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n =len(palindrome)
        if n == 1:
            return ""

        for i in range(n//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]

        if palindrome != "":
            for i in range(n-1,-1,-1):
                if palindrome[i] < 'z':
                    return (palindrome[:n-1] + chr(ord(palindrome[i]) + 1))
                    
        return ""
