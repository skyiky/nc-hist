from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
 
        ready = deque(
            course
            for course in range(numCourses)
            if indegree[course] == 0
        )

        completed = 0
        for i in indegree:
            if i == 0:
                completed += 1

        while ready:
            course = ready.popleft()
            for depn in graph[course]:
                indegree[depn] -= 1
                if indegree[depn] == 0:
                    completed += 1
                    ready.append(depn)
        
        return completed == numCourses