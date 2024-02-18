class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        art = ['+', '-', '*', '/']
        for i in tokens:
            if i in art:
                x = stack.pop()
                y = stack.pop()
                
                if i == '/':
                    c = int(y)/int(x)
                    z = (int(y)//int(x))
                    if z < 0 and z < c:
                        z+=1
                        z=z//1
                    print (y,x)
                else:
                    print(str(y) + i + str(x))
                    z = eval(str(y) + i + str(x))
                
                stack.append(z)
            else :
                stack.append(i)
        return (int(stack[0]))