class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Minimum possible speed is 1 banana/hour
        # Maximum possible speed is max(piles) (finish largest pile in 1 hour)
        l, r = 1, max(piles)

        # Store the best (minimum valid) speed found so far
        res = r

        while l <= r:
            # Try the middle speed
            k = (l + r) // 2

            # Calculate how many hours this speed would take
            totalTime = 0
            for p in piles:
                # For each pile, compute hours needed at speed k
                # We use ceil because even partial piles take a full hour
                totalTime += math.ceil(float(p) / k)

            # If we can finish within h hours,
            # this speed works (it is valid)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                # If it takes too long, speed is too slow
                # Increase speed
                l = k + 1

        return res
