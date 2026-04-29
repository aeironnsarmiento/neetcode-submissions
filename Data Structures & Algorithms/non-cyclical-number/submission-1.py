class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            total = 0

            for d in str(n):
                digit = int(d)
                square = digit * digit
                total += square

            n = total

        return n == 1