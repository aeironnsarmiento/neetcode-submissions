class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        grouped = {}

        for num in nums:
            grouped[num] = grouped.get(num, 0) + 1

        keys = list(grouped.keys())
        keys.sort(key=grouped.get, reverse=True)

        for i in range(k):
            res.append(keys[i])

        return res        