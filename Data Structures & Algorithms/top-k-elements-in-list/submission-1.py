class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        keys = list(freq.keys())
        keys.sort(key=freq.get, reverse=True)

        for i in range(k):
            ans.append(keys[i])

        return ans