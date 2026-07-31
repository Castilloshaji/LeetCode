#8. String to Integer (atoi)
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1

        if i < n and (s[i] == '+' or s[i] == '-'):

            if s[i] == '-':
                sign = -1

            i += 1

        num = 0

        while i < n and s[i].isdigit():

            digit = int(s[i])

            num = num * 10 + digit

            if sign * num < -2**31:
                return -2**31

            if sign * num > 2**31 - 1:
                return 2**31 - 1

            i += 1

        return sign * num
        