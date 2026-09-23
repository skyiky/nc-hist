class Solution:
    # Pattern 2: 
    # An undirected graph is a tree if it is connected and has exactly n - 1 edges.
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited: # skipping every visited neighbor is safe because DFS is only checking connectivity
                    dfs(neighbor)

        dfs(0)
        return len(visited) == n