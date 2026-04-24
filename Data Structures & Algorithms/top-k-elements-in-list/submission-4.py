class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        keys = list(count.keys())
        keys.sort(key=count.get, reverse=True)

        for i in range(k):
            res.append(keys[i])

        return res