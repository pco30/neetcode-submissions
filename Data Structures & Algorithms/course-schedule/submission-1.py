class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1
        
        count = 0
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            count+=1

            for neighbour in adj[course]:
                indegree[neighbour]-=1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if count == numCourses:
            return True
        
        return False
        