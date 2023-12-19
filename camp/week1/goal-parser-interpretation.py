class Solution:
    def interpret(self, command: str) -> str:
        out =""
        n=0
        while n < len(command):
            if command[n] == 'G':
                out += "G"
                n+=1
            elif command[n] == '(' and command[n+1] == ')':
                out += 'o'
                n+=2 
            elif command[n] == '(' and command[n+1] == 'a':
                out += "al"
                n+=4
        return (out)