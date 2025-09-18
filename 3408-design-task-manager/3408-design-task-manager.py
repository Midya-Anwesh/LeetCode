from heapq import heappush, heappop

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.userTasks = set()
        self.taskHeap = []
        self.taskToUPID = dict()
        for triplet in tasks:
            userId, taskId, priority = triplet
            self.userTasks.add((-priority, -taskId, userId))
            heappush(self.taskHeap, (-priority, -taskId, userId))
            self.taskToUPID[taskId] = [userId, priority]

    def add(self, userId: int, taskId: int, priority: int) -> None:
        if (-priority, -taskId, userId) in self.userTasks:
            return
        self.userTasks.add((-priority, -taskId, userId))
        heappush(self.taskHeap, (-priority, -taskId, userId))
        self.taskToUPID[taskId] = [userId, priority]

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId not in self.taskToUPID:
            return
        userId, oldPriority = self.taskToUPID[taskId]
        self.userTasks.remove((-oldPriority, -taskId, userId))
        self.userTasks.add((-newPriority, -taskId, userId))
        heappush(self.taskHeap, (-newPriority, -taskId, userId))
        self.taskToUPID[taskId] = [userId, newPriority]

    def rmv(self, taskId: int) -> None:
        if taskId not in self.taskToUPID:
            return
        userId, priority = self.taskToUPID[taskId]
        self.userTasks.remove((-priority, -taskId, userId))
        self.taskToUPID.pop(taskId)

    def execTop(self) -> int:
        while len(self.taskHeap):
            priority, taskId, userId = heappop(self.taskHeap)
            if (priority, taskId, userId) in self.userTasks:
                self.userTasks.remove((priority, taskId, userId))
                self.taskToUPID.pop(-taskId)
                return userId
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()