# runtime = 32.0ms
# memory usage = 16.6MB

class Solution:
    def __init__(self):
        self.hours = [8, 4, 2, 1]
        self.minutes = [32, 16, 8, 4, 2, 1]

    def gen_times(self, t, generated_times, h = 0, m = 0, h_index = 0, m_index = 0):
        if t == 0 or h >= 12 or m >= 60:
            if t == 0 and h < 12 and m < 60:
                generated_times.add(f"{h}:{m:0>2}")
            return
        for i in range(m_index, 6):
            self.gen_times(t-1, generated_times, h, m + self.minutes[i], h_index, i+1)
        for j in range(h_index, 4):
            self.gen_times(t-1, generated_times, h + self.hours[j], m, j+1, m_index)

    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        ret = set()
        self.gen_times(turnedOn,ret)
        return ret