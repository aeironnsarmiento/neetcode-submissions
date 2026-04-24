class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        group = {}

        for num in nums:
            group[num] = group.get(num, 0) + 1

        key = list(group.keys())
        key.sort(key=group.get, reverse=True)

        for i in range(k):
            res.append(key[i])

        return res