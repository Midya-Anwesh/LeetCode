class Solution:
    def maximumTime(self, time: str) -> str:
        hour, minute = time.split(":")
        if hour[0] == hour[1] == "?":
            hour = "23"
        elif hour[0] == "?":
            if hour[1] <= "3":
                hour = "2" + hour[1]
            else:
                hour = "1" + hour[1]
        elif hour[1] == "?":
            if hour[0] == "1":
                hour = "19"
            elif hour[0] == "0":
                hour = "09"
            elif hour[0] == "2":
                hour = "23"

        if minute[0] == minute[1] == "?":
            minute = "59"
        elif minute[0] == "?":
            minute = "5" + minute[1]
        elif minute[1] == "?":
            minute = minute[0] + "9"

        return f"{hour}:{minute}"