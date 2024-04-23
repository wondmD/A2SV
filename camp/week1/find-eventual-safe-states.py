class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0 for i in range(len(graph))]
        answer = []
        def dfs(index):
            if color[index] == 1:
                return False
            if color[index] == 2:
                return True
            color[index] = 1
            res = True
            for node in graph[index]:
                res = dfs(node) and res
            if res:
                answer.append(index)
                color[index] = 2
                return True
        for i in range(len(color)):
            if color[i] == 0:
                dfs(i)
        return sorted(answer)

            