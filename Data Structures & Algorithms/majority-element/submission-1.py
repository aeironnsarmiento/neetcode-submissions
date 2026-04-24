class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res = maxCount = 0

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]

        return res