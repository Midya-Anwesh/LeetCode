from math import floor, log
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        elif denominator == 1:
            return str(numerator)

        ret, decimalPlaced, lastSeenIdx, decimalUsed = "" if numerator * denominator >= 0 else "-", False, dict(), False
        numerator, denominator = abs(numerator), abs(denominator)
        while numerator > 0:
            lastSeenIdx[numerator] = len(ret)
            while numerator < denominator:
                if not decimalPlaced:
                    ret += "." if len(ret) > 0 else "0."
                    lastSeenIdx[numerator] = len(ret)
                    decimalPlaced = True
                    decimalUsed = True
                elif not decimalUsed :
                    decimalUsed = True
                else:
                    ret += "0"
                numerator *= 10
            decimalUsed = False

            multiplier = floor(numerator / denominator)
            if ((multiplier+1) * denominator) <= numerator:
                ret += str(multiplier+1)
                numerator -= (multiplier+1) * denominator
            else:
                ret += str(multiplier)
                numerator -= multiplier * denominator
            
            if numerator in lastSeenIdx:
                return ret[:lastSeenIdx[numerator]] + "(" + ret[lastSeenIdx[numerator]:]  + ")"
        return ret