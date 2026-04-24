class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        keys = list(freqMap.keys())
        keys.sort(key=freqMap.get, reverse=True)

        for i in range(k):
            res.append(keys[i])

        return res