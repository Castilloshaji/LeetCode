#7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x:

            digit = x % 10

            if rev > 214748364 or (rev == 214748364 and digit > 7):
                return 0

            rev = rev * 10 + digit
            x //= 10

        return sign * rev
        