class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            curSum = max(curSum, 0) + num
            maxSub = max(maxSub, curSum)
        return maxSub