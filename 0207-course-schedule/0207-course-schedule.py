from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree, child = {i:0 for i in range(numCourses)}, defaultdict(list)

        for u, v in prerequisites:
            inDegree[u] += 1
            child[v].append(u)
        
        startCourses = [course for course in inDegree if inDegree[course] == 0]
        courseCompleted = 0

        while len(startCourses):
            courseCompleted += 1
            currCourse = startCourses.pop(-1)
            for childCourse in child[currCourse]:
                inDegree[childCourse] -= 1
                if inDegree[childCourse] == 0:
                    startCourses.append(childCourse)
        
        return courseCompleted == numCourses
