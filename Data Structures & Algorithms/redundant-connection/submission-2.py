class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [x for x in range(n+1)] # [0, 1, 2, ..., n]
        size = [1 for _ in range(n+1)] #   [1, 1, 1, ..., 1]

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(node1: int, node2: int) -> bool:
            parent1 = find(node1)
            parent2 = find(node2)
            if parent1 == parent2:
                return False
            if size[parent1] > size[parent2]:
                parent1, parent2 = parent2, parent1 # parent2 always larger
            # add parent1 as child of parent2
            parent[parent1] = parent2
            size[parent2] += size[parent1]
            return True

        for node1, node2 in edges:
            success = union(node1, node2)
            if not success:
                return [node1, node2] # failed to union node1 and node2 meaning they were already in the same set

        return []