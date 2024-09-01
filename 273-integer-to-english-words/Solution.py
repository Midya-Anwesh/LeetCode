# runtime = 34.0ms
# memory usage = 16.6MB

# Class just to showcase heart of the program
class Str:
    
    # Heart of the program
    def to_str(self, num, num_to_word):
        if (num in num_to_word) and (num < 90):
            return num_to_word[num]
        ret :str
        for n in reversed(num_to_word.keys()):
            if n <= num:
                ret = num_to_word[n]
                if n > 90:
                    ret = self.to_str(num//n, num_to_word) + " " + ret
                if num % n != 0:
                    ret += " " + self.to_str(num%n, num_to_word)
                break
        return ret

class Solution:
    def numberToWords(self, num: int) -> str:
        word_dict = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }
        return Str().to_str(num, word_dict)