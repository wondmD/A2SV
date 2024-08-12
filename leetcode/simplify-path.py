
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_list = path.split('/')
        for i in path_list:
            if i == '..':
                if stack:
                    stack.pop()
            elif not ( i == '' or i=='.'):
                stack.append(i)
        return '/'+'/'.join(stack)

        