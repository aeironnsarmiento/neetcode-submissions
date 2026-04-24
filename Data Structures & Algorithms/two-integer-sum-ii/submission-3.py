class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numSet = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in numSet:
                return [numSet[diff] + 1, i + 1]
            numSet[numbers[i]] = i