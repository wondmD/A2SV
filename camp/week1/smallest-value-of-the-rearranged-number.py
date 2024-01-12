class Solution:
    def smallestNumber(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        if num < 0:
            num = abs(num)
            print (num)
            s = list(str(num)) 
            s2 = sorted(s, reverse=True)
            if s2[0] == '0':
                c = 1
                while True:
                    if s2[c] != '0':
                        s2[c], s2[0] = s2[0], s2[c]
                        break
                    c+=1
            s3 = int("".join(s2))
            return (-1*s3)
        else:
            s = list(str(num)) 
            s2 = sorted(s)
            if s2[0] == '0':
                c = 1
                while True:
                    if s2[c] != '0':
                        s2[c], s2[0] = s2[0], s2[c]
                        break
                    c+=1
            s3 = int("".join(s2))
            return(s3)
        #
                