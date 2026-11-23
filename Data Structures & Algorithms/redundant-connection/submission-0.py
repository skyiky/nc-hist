class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        
        def union(node1: int, node2: int) -> bool:
            p1 = find(node1)
            p2 = find(node2)

            if p1 == p2:
                return False
            
            if size[p1] < size[p2]:
                p1, p2 = p2, p1
            
            parent[p2] = p1
            size[p1] += size[p2]
            return True
            

        for n1, n2 in edges:
            union_result = union(n1, n2)
            if union_result == False:
                return [n1, n2]

        return []