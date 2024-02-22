class Solution:

    def decodeString(self, s: str) -> str:
        stack = []
        numstack =[]
        p = 0
        while p < len(s):
            if s[p].isdigit():
                dgs = s[p]
                p+=1
                while s[p].isdigit():
                    dgs += s[p]
                    p+=1
                numstack.append(int(dgs))
            elif s[p] == ']':
                l = []
                while stack:
                    if stack[-1] == '[':
                        stack.pop()
                        break
                    else:
                        l.append(stack.pop())
                x = numstack.pop()
                val = x * ("".join(l[::-1]))
                stack.append(val)
                p+=1
            else:
                stack.append(s[p])
                p+=1
        return "".join(stack)

