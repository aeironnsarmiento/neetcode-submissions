class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqMap = {}

        for num in nums:
            if num in freqMap and freqMap[num] >= 1:
                return True
            freqMap[num] = 1 + freqMap.get(num, 0)

        return False