class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        currTime = 0
        ret = [0 for _ in range(n)]
        waitingFuncs = []
        for log in logs:
            funcId, event, time = log.split(':')
            funcId, time = int(funcId), int(time)
            if event == "end":
                waitingFuncs.pop(-1)
                ret[funcId] += time - currTime + 1
                currTime = time + 1
            else:
                if len(waitingFuncs) >= 1:
                    prevFunc = waitingFuncs[-1]
                    ret[prevFunc] += time - currTime
                currTime = time
                waitingFuncs.append(funcId)
        return ret