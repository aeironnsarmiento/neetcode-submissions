class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in numMap:
                numMap[nums[i]] = i
            else:
                return [numMap[diff], i]