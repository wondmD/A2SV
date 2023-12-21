class Solution:
    def printVertically(self, s: str) -> List[str]:
        word_list = s.split()
        maxi = max(len(i) for i in word_list)
        output = []
        for i in range(maxi):
            vertical_word = ""
            for word in word_list:
                if i < len(word):
                    vertical_word+=word[i]
                else :
                    vertical_word+=" "
            output.append(vertical_word.rstrip())
        
        return (output)