class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        

        def combination(index, path):
            if len(path) == len(digits):
                if path:
                    res.append(''.join(path))
                return
            if index >= len(digits):
                return
            n = len(dic[digits[index]])
            
            for i in range(n):
                path.append(dic[digits[index]][i])
                combination(index + 1, path)
                path.pop()
        res = []
        combination(0, [])
        return res
