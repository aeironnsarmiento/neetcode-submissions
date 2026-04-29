class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            for d in str(n):
                dig = int(d)
                total += (dig * dig)

            n = total

        return n == 1