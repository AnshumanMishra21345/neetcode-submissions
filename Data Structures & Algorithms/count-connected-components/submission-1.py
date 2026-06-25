class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph={i:[] for i in range(n)}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited=set()
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        components=0
        for node in range(0,n):
            if node not in visited:
                components+=1
                dfs(node)
        return components