class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7:'pqrs', 8: "tuv", 9:'wxyz'}
        leng = len(digits)
        ans = []
        def backtrack(index,path):
            # print(path)
            if len(path)==leng:
                ans.append(''.join(path[:]))
                return
            if index >= leng:
                return
            for  i in dic[int(digits[index])]:
                # if index+1<leng:
                path.append(i)
                backtrack(index+1,path)
                path.pop()
        for i in range(leng):
            backtrack(i,[])
        return ans