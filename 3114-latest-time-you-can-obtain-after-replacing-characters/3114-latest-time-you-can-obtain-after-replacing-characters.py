class Solution:
    def findLatestTime(self, s: str) -> str:
        hour, minute = s.split(":")
        if hour[0] == hour[1] == "?":
            hour = "11"
        elif hour[0] == "?":
            if hour[1] <= "1":
                hour = "1" + hour[1]
            else:
                hour = "0" + hour[1]
        elif hour[1] == "?":
            if hour[0] == "0":
                hour = "09"
            else:
                hour = "11"

        if minute[0] == minute[1] == "?":
            minute = "59"
        elif minute[0] == "?":
            minute = "5" + minute[1]
        elif minute[1] == "?":
            minute = minute[0] + "9"

        return f"{hour}:{minute}"