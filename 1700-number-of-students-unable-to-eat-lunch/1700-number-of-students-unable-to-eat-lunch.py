from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        while len(students) and len(sandwiches):
            eaten = False
            swaps = 0
            while students[0] != sandwiches[0] and swaps < len(students):
                students.append(students.popleft())
                swaps += 1
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                eaten = True
            if not eaten:
                return len(students)
        return 0