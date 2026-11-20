from collections import Counter
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # firstly... need to get list of courses that DON'T have prerequisites.. start from them
        # these are courses that have indegree == 0

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for c2, c1 in prerequisites:
            graph[c1].append(c2)
            indegree[c2] += 1

        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)

        completed = 0
        while q: # if no availabe courses then cannot continue, termination condition is when we have taken all courses
            # take the course
            took = q.popleft()
            completed += 1 
            # subtract indegree for each course that listed this course as a prerequisite
            for c in graph[took]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c) # we can take now
            

        return completed == numCourses
        