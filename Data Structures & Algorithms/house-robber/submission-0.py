class Solution:
    def rob(self, nums: List[int]) -> int:
        x, y = 0, 0

        for num in nums:
            x, y = y, max(num + x, y)

        return y