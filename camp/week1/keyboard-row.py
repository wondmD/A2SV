class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop','asdfghjkl','zxcvbnm']
        out =[]
        n = len(words)
        for i in range(n):
            word = words[i]
            f = 1
            if word[0].lower() in rows[0]:
                for letter in word:
                    if letter.lower() not in rows[0]:
                        f = 0
                        break
                if f ==1 :
                    out.append(word)
            elif word[0].lower() in rows[1]:
                for letter in word:
                    if letter.lower() not in rows[1]:
                        f = 0
                        break
                if f ==1 :
                    out.append(word)
            elif word[0].lower() in rows[2]:
                for letter in word:
                    if letter.lower() not in rows[2]:
                        f = 0
                        break
                if f ==1 :
                    out.append(word)
        return (out)

            
                    
        return (out)

        