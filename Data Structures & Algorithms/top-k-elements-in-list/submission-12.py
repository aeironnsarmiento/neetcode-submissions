class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        keys = list(freq.keys())
        keys.sort(key=freq.get, reverse=True)

        for i in range(k):
            res.append(keys[i])

        return res